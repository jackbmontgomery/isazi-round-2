// @ts-ignore
import CanvasJSChart from '@canvasjs/vue-charts';

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(CanvasJSChart);
});