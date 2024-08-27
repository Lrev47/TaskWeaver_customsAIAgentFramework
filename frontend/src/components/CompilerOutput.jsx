import React from "react";
import { Box, Paper, Typography } from "@mui/material";

const CompilerOutput = ({ output }) => {
  return (
    <Paper sx={{ p: 3, mt: 2 }}>
      <Typography variant="h6" component="div">
        Compiler Output
      </Typography>
      <Box sx={{ mt: 2 }}>
        <Typography variant="body1" component="pre">
          {output}
        </Typography>
      </Box>
    </Paper>
  );
};

export default CompilerOutput;
