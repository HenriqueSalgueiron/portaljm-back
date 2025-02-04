const functions = require("firebase-functions");
const { createProxyMiddleware } = require("http-proxy-middleware");

const apiProxy = createProxyMiddleware({
  target: "https://portal-jonas-madureira.web.app", // URL do seu servidor Django
  changeOrigin: true,
});

exports.djangoBackend = functions.https.onRequest((req, res) => {
  apiProxy(req, res);
});
