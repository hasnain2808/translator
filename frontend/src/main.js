import { createApp } from "vue";
import { FrappeUI, Button, Alert } from "frappe-ui";
import App from "./App.vue";
import "./index.css";

const app = createApp(App)

app.use(FrappeUI);
app.component("Button", Button);
app.component("Alert", Alert);

app.mount("#app");
