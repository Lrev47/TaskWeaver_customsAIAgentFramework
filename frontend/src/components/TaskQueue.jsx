import React from "react";
import {
  Paper,
  Typography,
  List,
  ListItem,
  ListItemText,
  LinearProgress,
} from "@mui/material";

const TaskQueue = () => {
  const tasks = [
    { id: 1, description: "Analyzing text data", progress: 60 },
    { id: 2, description: "Processing image data", progress: 80 },
    // Add more tasks as needed
  ];

  return (
    <Paper sx={{ p: 3 }}>
      <Typography variant="h6" component="div">
        Task Queue
      </Typography>
      <List>
        {tasks.map((task) => (
          <ListItem key={task.id}>
            <ListItemText
              primary={task.description}
              secondary={
                <LinearProgress variant="determinate" value={task.progress} />
              }
            />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
};

export default TaskQueue;
