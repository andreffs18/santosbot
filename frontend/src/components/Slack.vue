<template>
  <div id="slack-container">
    <div id="sidebar">
      <div id="team-picker">
        <ul class="teams">
          <li class="team" />
        </ul>
      </div>
      <div id="team-name">
        <h1>andreffs</h1>
      </div>
      <div id="username">
        <div class="status"></div>
        <h2>andreffs18</h2>
      </div>
      <ul id="channels">
        <h4>channels</h4>
        <li class="channel selected">
          <p><i>#</i>general</p>
        </li>
        <li class="channel unread">
          <p><i>#</i>random</p>
        </li>
        <li class="channel">
          <p><i>#</i>memes</p>
        </li>
      </ul>
      <ul id="direct-messages">
        <h4>Direct Messages</h4>
        <li class="direct-message">
          <div class="status"></div>
          <p>slackbot</p>
        </li>
        <li class="direct-message">
          <div class="status"></div>
          <p>gustavo-santos</p>
        </li>
        <li class="direct-message andreffs18">
          <div class="status inactive"></div>
          <p>andreffs18</p>
        </li>
      </ul>
    </div>
    <div id="chat">
      <div class="header-bar">
        <h1>#general</h1>
        <div class="details">
          <h3 class="members">3 members</h3>
          <h3 class="purpose">Almost like random</h3>
        </div>
      </div>
      <div id="chatbox">
        <ul class="messages">
          <li v-bind:key="message" v-for="message in messages">
            <SlackMessage
              :url="message.url"
              :text="message.text"
              :username="message.username"
            />
          </li>
        </ul>
      </div>
      <div class="input-bar">
        <form v-on:submit.prevent>
          <input
            autofocus
            v-on:keyup.enter="submitMessage"
            type="text"
            v-model="text"
            placeholder="Message #general"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import SlackMessage from "./SlackMessage";
const axios = require("axios");

export default {
  components: {
    SlackMessage
  },
  data() {
    return {
      isActive: false,
      text: "Olá mundo!",
      messages: [
        {
          url: require("../assets/images/santosbot.jpeg"),
          username: "Gustavo Santos",
          text: "@channel A liberdade é o expoente máximo do amor-próprio."
        },
        {
          url: require("../assets/images/santosbot.jpeg"),
          username: "Gustavo Santos",
          text: "Para ser como os outros prefiro assumir que não sou ninguém."
        }
      ]
    };
  },
  updated() {
    const container = this.$el.querySelector("#chatbox");
    container.scrollTop = container.scrollHeight;
  },
  mounted() {
    window.addEventListener(
      "keypress",
      function() {
        if (this.isActive) {
          return;
        }
        this.isActive = true;

        const status = this.$el.querySelector(
          "li.direct-message.andreffs18 div"
        );
        status.classList = ["status"];

        setTimeout(() => {
          this.isActive = false;
          status.classList = ["status inactive"];
        }, 30000);
      }.bind(this)
    );
  },
  methods: {
    submitMessage: function() {
      // only proceed if any message was submitted
      if (this.text.trim().length === 0) {
        return;
      }

      this.messages.push({
        username: "andreffs",
        url: require("../assets/images/andreffs.jpeg"),
        text: this.text.trim()
      });
      this.postMessage();
      // clean message input and scroll down chatbox
      this.text = "";
    },
    postMessage: function() {
      console.log(this.text);
      axios
        .get(process.env.VUE_APP_API_URL + "/bot?text=" + this.text)
        .then(response => {
          console.log(response);
          if (response.data.quote === "") {
            return;
          }
          this.messages.push({
            username: "Gustavo Santos",
            url: require("../assets/images/santosbot.jpeg"),
            text: response.data.quote
          });
        });
    }
  }
};
</script>

<style lang="scss" scoped>
@import "src/assets/css/slack.scss";
</style>
