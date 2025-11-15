import React from 'react';
import './Commands.css';

function Commands() {
  const commands = [
    { name: '!kick', description: 'Kick a member from the server', usage: '!kick @user [reason]' },
    { name: '!ban', description: 'Permanently ban a member', usage: '!ban @user [reason]' },
    { name: '!unban', description: 'Remove a ban from a user', usage: '!unban username' },
    { name: '!mute', description: 'Timeout a member', usage: '!mute @user <minutes> [reason]' },
    { name: '!unmute', description: 'Remove timeout from a member', usage: '!unmute @user' },
    { name: '!clear', description: 'Delete messages in bulk', usage: '!clear <amount>' },
    { name: '!stats', description: 'Display server statistics', usage: '!stats' },
    { name: '!help', description: 'Show all commands', usage: '!help' },
  ];

  return (
    <div className="commands">
      <h1 className="page-title">Commands</h1>
      
      <div className="commands-grid">
        {commands.map((cmd, index) => (
          <div key={index} className="command-card">
            <h3 className="command-name">{cmd.name}</h3>
            <p className="command-description">{cmd.description}</p>
            <div className="command-usage">
              <span>Usage:</span>
              <code>{cmd.usage}</code>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Commands;
