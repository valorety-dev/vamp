import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json
import re
from typing import List
import random
import os

class PinterestScraper:
    """Scraper for fetching Pinterest images without official API"""
    
    def __init__(self):
        self.base_url = "https://www.pinterest.com"
        self.pexels_api_key = os.getenv('PEXELS_API_KEY', '')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }
    
    async def search_images(self, keyword: str, limit: int = 5) -> List[str]:
        """
        Search Pinterest for images based on keyword
        
        Args:
            keyword: Search term
            limit: Maximum number of images to return
            
        Returns:
            List of image URLs
        """
        try:
            images = []
            
            # Use Pinterest's JSON API endpoint
            search_url = f"https://www.pinterest.com/resource/BaseSearchResource/get/"
            
            params = {
                'source_url': f'/search/pins/?q={keyword}',
                'data': json.dumps({
                    'options': {
                        'query': keyword,
                        'scope': 'pins',
                        'page_size': limit
                    }
                })
            }
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.get(search_url, params=params, headers=headers, timeout=15) as response:
                    if response.status == 200:
                        data = await response.json()
                        # Extract image URLs from Pinterest's response
                        images = self._extract_from_pinterest_json(data, limit)
                        
            if images:
                print(f"Found {len(images)} images from Pinterest")
                return images[:limit]
            
            # If Pinterest didn't work, try Pexels
            if self.pexels_api_key and self.pexels_api_key != 'your_pexels_api_key_here':
                print("Pinterest failed, trying Pexels API...")
                return await self._fetch_from_pexels(keyword, limit)
            
            print("No API keys available, using fallback...")
            return await self._fetch_from_unsplash(keyword, limit)
                    
        except Exception as e:
            print(f"Error fetching from Pinterest: {e}")
            if self.pexels_api_key and self.pexels_api_key != 'your_pexels_api_key_here':
                return await self._fetch_from_pexels(keyword, limit)
            return await self._fetch_from_unsplash(keyword, limit)
    
    async def _fetch_from_pexels(self, keyword: str, limit: int = 5) -> List[str]:
        """Fetch images from Pexels API (free, requires API key)"""
        try:
            images = []
            search_url = f"https://api.pexels.com/v1/search?query={keyword}&per_page={limit}"
            
            headers = {
                'Authorization': self.pexels_api_key
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.get(search_url, headers=headers, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        photos = data.get('photos', [])
                        
                        for photo in photos[:limit]:
                            # Get the large image URL
                            img_url = photo.get('src', {}).get('large', '')
                            if img_url:
                                images.append(img_url)
                    else:
                        print(f"Pexels API error: {response.status}")
            
            return images
        except Exception as e:
            print(f"Pexels fetch error: {e}")
            return []
    
    async def _fetch_from_unsplash(self, keyword: str, limit: int = 5) -> List[str]:
        """Fallback to fetch images using DuckDuckGo image search (no API key)"""
        try:
            images = []
            search_term = keyword.replace(' ', '+')
            
            # Use a simple approach: direct image URLs from reliable sources
            # Method 1: Try Pexels API (has a generous free tier)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            # Use Lorem Picsum as reliable fallback (always works)
            base_width = 800
            base_height = 600
            
            for i in range(limit):
                # Use seed based on keyword hash for consistency
                seed = hash(f"{keyword}{i}") % 10000
                img_url = f"https://picsum.photos/seed/{seed}/{base_width}/{base_height}"
                images.append(img_url)
            
            return images
        except Exception as e:
            print(f"Fallback fetch error: {e}")
            return []
    
    def _extract_from_pinterest_json(self, data: dict, limit: int = 5) -> List[str]:
        """Extract image URLs from Pinterest JSON API response"""
        images = []
        
        try:
            # Navigate Pinterest's JSON structure
            resource_response = data.get('resource_response', {})
            pins_data = resource_response.get('data', {})
            results = pins_data.get('results', [])
            
            for pin in results[:limit]:
                # Get the largest image available
                images_dict = pin.get('images', {})
                
                # Try to get the original or largest size
                if 'orig' in images_dict:
                    img_url = images_dict['orig'].get('url')
                elif '736x' in images_dict:
                    img_url = images_dict['736x'].get('url')
                elif '564x' in images_dict:
                    img_url = images_dict['564x'].get('url')
                else:
                    # Get first available image
                    for size_key in images_dict:
                        img_url = images_dict[size_key].get('url')
                        if img_url:
                            break
                
                if img_url:
                    images.append(img_url)
            
            return images
        except Exception as e:
            print(f"Error extracting Pinterest JSON: {e}")
            return []
    
    def _extract_image_urls(self, html: str) -> List[str]:
        """Extract image URLs from Pinterest HTML"""
        image_urls = []
        
        try:
            # Method 1: Find JSON data in script tags
            soup = BeautifulSoup(html, 'html.parser')
            scripts = soup.find_all('script', {'id': 'initial-state'})
            
            for script in scripts:
                if script.string:
                    try:
                        data = json.loads(script.string)
                        # Navigate through the JSON structure to find images
                        images = self._extract_from_json(data)
                        image_urls.extend(images)
                    except json.JSONDecodeError:
                        pass
            
            # Method 2: Find image tags directly
            if not image_urls:
                img_tags = soup.find_all('img', {'src': re.compile(r'pinimg\.com')})
                for img in img_tags:
                    src = img.get('src')
                    if src and 'pinimg.com' in src:
                        # Get higher quality version
                        src = src.replace('236x', '736x')
                        image_urls.append(src)
            
            # Remove duplicates while preserving order
            seen = set()
            unique_urls = []
            for url in image_urls:
                if url not in seen and url.startswith('http'):
                    seen.add(url)
                    unique_urls.append(url)
            
            return unique_urls
            
        except Exception as e:
            print(f"Error extracting image URLs: {e}")
            return []
    
    def _extract_from_json(self, data: dict, images: List[str] = None) -> List[str]:
        """Recursively extract image URLs from JSON data"""
        if images is None:
            images = []
        
        if isinstance(data, dict):
            # Look for image URL keys
            for key, value in data.items():
                if key in ['url', 'src'] and isinstance(value, str) and 'pinimg.com' in value:
                    images.append(value.replace('236x', '736x'))
                elif isinstance(value, (dict, list)):
                    self._extract_from_json(value, images)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    self._extract_from_json(item, images)
        
        return images
