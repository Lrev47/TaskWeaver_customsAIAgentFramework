import React, { useState } from "react";
import { TextField, Button, Paper, Typography } from "@mui/material";

const UserInputForm = ({ onSubmit }) => {
  const [inputValue, setInputValue] = useState("");

  const handleSubmit = () => {
    onSubmit(inputValue);
    setInputValue("");
  };

  return (
    <Paper sx={{ p: 3, mt: 2 }}>
      <Typography variant="h6" component="div">
        User Input
      </Typography>
      <TextField
        label="Enter your task"
        fullWidth
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        sx={{ mt: 2, mb: 2 }}
      />
      <Button variant="contained" color="primary" onClick={handleSubmit}>
        Submit
      </Button>
    </Paper>
  );
};

export default UserInputForm;
