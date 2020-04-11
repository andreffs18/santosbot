<template>
  <div id="profileContainer">
    <div id="profile">
      <header>
        <div class="avatar">
          <img
            class="avatarMask"
            src="../assets/images/avatar.jpg"
            alt="Olha-me p&#39;este fofo!"
          />
        </div>
        <h1 class="author">Santosbot</h1>
      </header>
      <p>Motivational bot for your everyday use</p>
      <nav>
        <ul>
          <li v-bind:key="link" v-for="link in links">
            <a :href="link.href" :aria-label="link.label" target="_blank">
              <i :class="link.class" /><br />
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      links: [
        {
          label: "blog",
          href: "http://blog.andreffs.com/#",
          class: "fa fa-book-open fa-lg"
        },
        {
          label: "twitter",
          href: "https://twitter.com/andreffs18",
          class: "fab fa-twitter fa-lg"
        },
        {
          label: "github",
          href: "https://github.com/andreffs18/santosbot",
          class: "fab fa-github fa-lg"
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
@import "src/assets/css/hellocard.scss";
</style>
