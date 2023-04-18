import './App.css';
import FileUpload from './components/FileUpload';
import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import Chat from './components/Chat';
import './App.css';

function App() {
  const [summary, setSummary] = useState('');

  return (
    <div className="App">
      {!summary ? (
        <UploadForm onSummary={(summary) => setSummary(summary)} />
      ) : (
        <Chat summary={summary} />
      )}
    </div>
  );
}

export default App;
