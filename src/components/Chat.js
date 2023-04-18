import React, { useState } from 'react';
import axios from 'axios';
import { Button, InputGroup, Input, Form, ListGroup, ListGroupItem } from 'reactstrap';

const Chat = ({ summary }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setMessages([...messages, { role: 'user', content: input }]);
    setInput('');

    try {
      const response = await axios.post('http://localhost:5000/chat', {
        input: input,
        summary: summary,
      });
      setMessages([
        ...messages,
        { role: 'user', content: input },
        { role: 'assistant', content: response.data.message },
      ]);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="chat-container">
      <ListGroup className="messages mb-3">
        {messages.map((message, index) => (
          <ListGroupItem
            key={index}
            className={`message ${message.role === 'user' ? 'text-end' : 'text-start'}`}
          >
            {message.content}
          </ListGroupItem>
        ))}
      </ListGroup>
      <Form onSubmit={handleSubmit}>
        <InputGroup>
          <Input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask a question about the book"
          />
          <div className="input-group-append">
            <Button type="submit" color="primary">
              Send
            </Button>
          </div>
        </InputGroup>
      </Form>
    </div>
  );
};

export default Chat;