import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../../services/api";

export const fetchAgents = createAsyncThunk("agents/fetchAgents", async () => {
  const response = await api.get("/agents");
  return response.data;
});

const agentsSlice = createSlice({
  name: "agents",
  initialState: {
    agents: [],
    status: "idle",
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchAgents.pending, (state) => {
        state.status = "loading";
      })
      .addCase(fetchAgents.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.agents = action.payload;
      })
      .addCase(fetchAgents.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message;
      });
  },
});

export default agentsSlice.reducer;
