import axios from "axios";

// Create an instance of axios with a base URL
const api = axios.create({
  baseURL: "http://localhost:8000", // Replace with your actual backend URL
  headers: {
    "Content-Type": "application/json",
  },
});

// Example of a GET request
export const getAgents = async () => {
  const response = await api.get("/agents");
  return response.data;
};

// Example of a POST request
export const runAgent = async (agentId, payload) => {
  const response = await api.post(`/agents/${agentId}/run`, payload);
  return response.data;
};

export default api;
