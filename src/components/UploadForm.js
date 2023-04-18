import React, { useRef } from 'react';
import axios from 'axios';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

const UploadForm = ({ onSummary }) => {
  const fileInput = useRef();

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file', fileInput.current.files[0]);

    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.summary) {
        onSummary(response.data.summary);
      }
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div className="container">
      <h1 className="text-center my-5">Upload Your eBook</h1>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label htmlFor="file">Upload an EPUB file:</Label>
          <Input type="file" id="file" name="file" innerRef={fileInput} />
        </FormGroup>
        <Button type="submit" color="primary">Upload</Button>
      </Form>
    </div>
  );
};

export default UploadForm;
