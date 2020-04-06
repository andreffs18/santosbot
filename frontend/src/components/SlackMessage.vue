<template>
  <li class="message">
    <div class="user-icon"><img :src="url" /></div>
    <div class="body">
      <div class="username">{{ username }}</div>
      <div class="text">{{ text }}</div>
    </div>
  </li>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: ["url", "username", "text"]
};
</script>
>

<style lang="scss" scoped>
$SlackTeal: #4c9689;
$SlackPurple: #4e394c;

.message {
  display: flex;
  padding: 10px 10px 10px 20px;
  font-size: 14px;

  .user-icon {
    position: relative;
    top: 4px;
    margin-right: 7px;
    width: 35px;
    height: 35px;
    border-radius: 4px;
    overflow: hidden;
    background: $SlackPurple;
    display: inline-block;

    img {
      width: 100%;
      height: auto;
    }
  }

  .body {
    display: inline-block;
    width: 80%;
    top: 0;

    .username {
      font-weight: 700;
      padding-bottom: 3px;
    }

    .text {
      color: #252525;
    }
  }
}
</style>
