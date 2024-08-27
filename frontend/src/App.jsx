import React from "react";
import { Provider } from "react-redux";
import { store } from "./store/store";
import Dashboard from "./components/Dashboard";
import { CssBaseline, ThemeProvider, createTheme } from "@mui/material";

// Optional: Custom theme
const theme = createTheme({
  palette: {
    mode: "light",
  },
});

const App = () => {
  return (
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Dashboard />
      </ThemeProvider>
    </Provider>
  );
};

export default App;
