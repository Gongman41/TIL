<template>
  <div class="background-container bg-img">
    <form id="msform" @submit.prevent="login">
      <fieldset>
        <h2 class="fs-title">Login</h2>
        <h3 class="fs-subtitle">로그인</h3>
        <input type="text" v-model.trim="username" placeholder="아이디" />
        <input type="password" v-model.trim="password" id="password" placeholder="비밀번호" />
        <input type="submit" name="login" class="next action-button" value="로그인" />
        <RouterLink :to="{ name: 'SignUp' }" class="next action-button">회원가입</RouterLink>
      </fieldset>
    </form>
  </div>
</template>
<!-- 
<template>
  <div class="background-container bg-img">
    <form @submit.prevent="login" class="signup-form">
      <div style="border-bottom: 1px solid red; width: 100%; text-align: center;">
        <h1 class="title">로그인</h1>
      </div>
      <div>
        <p><label class="label" for="username">아이디</label></p>
        <input type="text" v-model.trim="username" id="username" class="input-box">
      </div>
      <div>
        <p><label class="label" for="password">비밀번호</label></p>
        <input type="password" v-model.trim="password" id="password" class="input-box">
      </div>
      <div class="button-container">
        <input type="submit" value="로그인" class="signup-button">
        <RouterLink :to="{ name: 'SignUp' }" class="signup-button">회원가입</RouterLink>
      </div>
    </form>
  </div>
</template> -->

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useMemberStore } from '@/stores/member'
import $ from 'jquery'
import 'jquery.easing'

const username = ref(null)
const password = ref(null)
const memberStore = useMemberStore()

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  memberStore.login(payload)
}
onMounted(() => {
  var current_fs, next_fs, previous_fs
  var left, opacity, scale
  var animating

  $(".next").click(function () {
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

    next_fs.show();
    current_fs.animate({ opacity: 0 }, {
      step: function (now, mx) {
        scale = 1 - (1 - now) * 0.2;
        left = (now * 50) + "%";
        opacity = 1 - now;
        current_fs.css({
          'transform': 'scale(' + scale + ')',
          'position': 'absolute'
        });
        next_fs.css({ 'left': left, 'opacity': opacity });
      },
      duration: 800,
      complete: function () {
        current_fs.hide();
        animating = false;
      },
      easing: 'easeInOutBack'
    });
  });

  $(".previous").click(function () {
    if (animating) return false;
    animating = true;

    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

    previous_fs.show();
    current_fs.animate({ opacity: 0 }, {
      step: function (now, mx) {
        scale = 0.8 + (1 - now) * 0.2;
        left = ((1 - now) * 50) + "%";
        opacity = 1 - now;
        current_fs.css({ 'left': left });
        previous_fs.css({ 'transform': 'scale(' + scale + ')', 'opacity': opacity });
      },
      duration: 800,
      complete: function () {
        current_fs.hide();
        animating = false;
      },
      easing: 'easeInOutBack'
    });
  });
});
</script>

<style scoped>
.button-container {
  background-image: url('@/assets/glasses.png');
  display: flex;
  width: 100%;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
}

.title {
  color: white;
  font-size: 32px;
  margin-bottom: 20px;
}

.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #af787b;
  margin: 100px;
  /* background-color: rgba(0, 0, 0, 0.5); */
  padding: 20px;
  border-radius: 10px;
}

.label {
  font-size: 20px;
  font-weight: bold;
  color: white;
}

.input-box {
  background: #f5f7fe;
  /* 살짝 투명하게 설정 */
  color: black;
  font-size: 20px;
  width: 300px;
  height: 40px;
  border-radius: 10px;
  padding-left: 10px;
  margin-bottom: 10px;
}

.signup-button {
  /* background: linear-gradient(to bottom, #c9b6b4, #af787b); */
  background-color: red;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
  text-align: center;
  text-decoration: none;
}

.background-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  color: #3D3D3D;
}

.bg-img {
  background-image: url('@/assets/dong.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  background-color: #f5f7fe;
}

/* form styles */
#msform {
  width: 400px;
  margin: 50px auto;
  text-align: center;
  position: relative;
  margin-right: auto;
  /* 오른쪽 여백 추가 */
  margin-left: 40px;
  /* 왼쪽 정렬 */
}

#msform fieldset {
  background: white;
  border: 0 none;
  border-radius: 3px;
  box-shadow: 0 0 15px 1px rgba(0, 0, 0, 0.4);
  padding: 20px 30px;
  box-sizing: border-box;
  width: 80%;
  margin: 0 10%;
  /* stacking fieldsets above each other */
  position: relative;
}

/* Hide all except first fieldset */
#msform fieldset:not(:first-of-type) {
  display: none;
}

/* inputs */
#msform input,
#msform textarea {
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px;
  width: 100%;
  box-sizing: border-box;
  font-family: montserrat;
  color: #2C3E50;
  font-size: 13px;
}

/* buttons */
#msform .action-button {
  width: 100px;
  background: #27AE60;
  font-weight: bold;
  color: white;
  border: 0 none;
  border-radius: 1px;
  cursor: pointer;
  padding: 10px;
  margin: 10px 5px;
  text-decoration: none;
  font-size: 14px;
}

#msform .action-button:hover,
#msform .action-button:focus {
  box-shadow: 0 0 0 2px white, 0 0 0 3px #27AE60;
}

/* headings */
.fs-title {
  font-size: 15px;
  text-transform: uppercase;
  color: #2C3E50;
  margin-bottom: 10px;
}

.fs-subtitle {
  font-weight: normal;
  font-size: 13px;
  color: #666;
  margin-bottom: 20px;
}

/* progressbar */
#progressbar {
  margin-bottom: 30px;
  overflow: hidden;
  /* CSS counters to number the steps */
  counter-reset: step;
}

#progressbar li {
  list-style-type: none;
  color: white;
  text-transform: uppercase;
  font-size: 9px;
  width: 33.33%;
  float: left;
  position: relative;
}

#progressbar li:before {
  content: counter(step);
  counter-increment: step;
  width: 20px;
  line-height: 20px;
  display: block;
  font-size: 10px;
  color: #333;
  background: white;
  border-radius: 3px;
  margin: 0 auto 5px auto;
}

/* progressbar connectors */
#progressbar li:after {
  content: '';
  width: 100%;
  height: 2px;
  background: white;
  position: absolute;
  left: -50%;
  top: 9px;
  z-index: -1;
  /* put it behind the numbers */
}

#progressbar li:first-child:after {
  /* connector not needed before the first step */
  content: none;
}

/* marking active/completed steps green */
/* The number of the step and the connector before it = green */
#progressbar li.active:before,
#progressbar li.active:after {
  background: #27AE60;
  color: white;
}
</style>
