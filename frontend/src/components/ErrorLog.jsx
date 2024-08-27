import React from "react";
import { Paper, Typography, List, ListItem, ListItemText } from "@mui/material";

const ErrorLog = () => {
  const errors = [
    { id: 1, message: "Error processing image data." },
    { id: 2, message: "Failed to compile the output." },
    // Add more errors as needed
  ];

  return (
    <Paper sx={{ p: 3, mt: 2 }}>
      <Typography variant="h6" component="div">
        Error Log
      </Typography>
      <List>
        {errors.map((error) => (
          <ListItem key={error.id}>
            <ListItemText primary={error.message} />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
};

export default ErrorLog;
