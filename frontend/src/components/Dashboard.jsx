import React from "react";
import { Grid, Container, Typography } from "@mui/material";
import TaskQueue from "./TaskQueue";
import ErrorLog from "./ErrorLog";
import AgentCard from "./AgentCard";
import CompilerOutput from "./CompilerOutput";

const Dashboard = () => {
  const agents = [
    {
      title: "Deconstructor Agent",
      description: "Breaks down tasks into smaller tasks.",
    },
    {
      title: "Compiler Agent",
      description: "Compiles data into a final document.",
    },
    // Add more agents as needed
  ];

  const handleAgentAction = (agent) => {
    console.log(`Running agent: ${agent}`);
  };

  return (
    <Container sx={{ mt: 5 }}>
      <Typography variant="h4" gutterBottom>
        Agent HiveMind Dashboard
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <TaskQueue />
          <ErrorLog />
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography variant="h5" gutterBottom>
            Agents
          </Typography>
          <Grid container spacing={2}>
            {agents.map((agent, index) => (
              <Grid item xs={12} sm={6} key={index}>
                <AgentCard
                  title={agent.title}
                  description={agent.description}
                  onAction={() => handleAgentAction(agent.title)}
                />
              </Grid>
            ))}
          </Grid>
          <CompilerOutput output="Compiled output will be shown here." />
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
