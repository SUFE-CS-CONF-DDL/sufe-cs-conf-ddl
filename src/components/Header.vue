<template>
    <section>
        <el-row>
            <a href="/" class="title">SUFE SIME Tenure Track CS Conference Deadlines</a>
            <github-button style="padding-left: 5px"></github-button>
            <span v-if="showLatestConf" style="color:#fd3c95;font-weight: bold;">
              Latest: {{this.showStr}} !!!
            </span>
        </el-row>
        <el-row class = 'subtitle'>
            Countdowns to tenure track cs conference. To add/edit a conference, <a style="color: #666666" href="https://github.com/SUFEHeisenberg/sufe-cs-conf-ddl/pulls">send a pull request.</a>
        </el-row>
    </section>
</template>

<script>
import GithubButton from './GithubButton.vue';

export default {
  name: 'Header',
  components: { GithubButton },
  data() {
    return {
      showLatestConf: false,
      showStr: '',
    };
  },
  mounted() {
    this.$help.get('https://api.github.com/repos/SUFEHeisenberg/sufe-cs-conf-ddl/commits?page=1&per_page=10').then((response) => {
      const len = response.body.length;

      for (let i = 0; i < len; i += 1) {
        let str = response.body[i].commit.message;
        const strArr = str.split(' ');
        const idx = str.indexOf('(');
        if (strArr[0] === 'Update') {
          if (idx !== -1) {
            str = str.substr(0, idx);
          }
          this.showStr = str;
          this.showLatestConf = true;
          break;
        }
      }
    });
  },
};
</script>

<style scoped>
.title{
  font-size: 29px;
  color: #2c3e50;
}
.subtitle{
  padding-top: 15px;
  color: #666666;
}
</style>
