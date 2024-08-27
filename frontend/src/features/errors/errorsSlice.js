import { createSlice } from "@reduxjs/toolkit";

const errorsSlice = createSlice({
  name: "errors",
  initialState: {
    errors: [],
  },
  reducers: {
    logError: (state, action) => {
      state.errors.push(action.payload);
    },
    clearErrors: (state) => {
      state.errors = [];
    },
  },
});

export const { logError, clearErrors } = errorsSlice.actions;
export default errorsSlice.reducer;
