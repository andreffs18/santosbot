<template>
  <div id="app">
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.2.0/css/all.css"
      integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ"
      crossorigin="anonymous"
    />
    <HelloCard></HelloCard>
    <Slack></Slack>
    <div style="clear:both;"></div>
  </div>
</template>

<script>
import HelloCard from "./components/HelloCard.vue";
import Slack from "./components/Slack.vue";

export default {
  name: "App",
  components: {
    HelloCard,
    Slack
  },
  data() {
    return {};
  }
};
</script>

<style lang="scss">
@import "src/assets/css/background.scss";
@import "src/assets/css/app.scss";
</style>
