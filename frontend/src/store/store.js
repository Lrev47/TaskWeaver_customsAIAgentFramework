import { configureStore } from "@reduxjs/toolkit";
import agentsReducer from "../features/agents/agentsSlice";
import errorsReducer from "../features/errors/errorsSlice";
import userReducer from "../features/user/userSlice";

const store = configureStore({
  reducer: {
    agents: agentsReducer,
    errors: errorsReducer,
    user: userReducer,
  },
});

export default store;
