<template>
    <div class="background-container bg-img">
        <form id="msform" @submit.prevent="signup">
            <ul id="progressbar">
                <li class="active">회원 정보</li>
                <li>장르 선택</li>
                <li>가입 완료</li>
            </ul>
            <fieldset>
                <h2 class="fs-title">Create your account</h2>
                <h3 class="fs-subtitle">회원 정보</h3>
                <input type="text" v-model.trim="username" placeholder="아이디" />
                <input type="password" v-model.trim="password1" id="password1" placeholder="비밀번호" />
                <input type="password" v-model.trim="password2" id="password2" placeholder="비밀번호 확인" />
                <input type="text" v-model.trim="nickname" id="nickname" placeholder="닉네임" />
                <input type="button" name="next" class="next action-button" value="Next" />
            </fieldset>
            <fieldset>
                <h2 class="fs-title">Choose your favorite genres</h2>
                <h3 class="fs-subtitle">좋아하는 영화 장르</h3>
                <div class="genre-checkboxes">
                    <div>
                        <div v-for="genre in movieStore.genres.slice(0, 10)" :key="genre.pk">
                            <input type="checkbox" :id="genre.name" :value="genre.id" v-model="choosenGenres"
                                value="genre.name" class="genre-checkbox">
                            <label :for="genre.name">{{ genre.name }}</label>
                        </div>
                    </div>
                    <div>
                        <div v-for="genre in movieStore.genres.slice(10)" :key="genre.pk">
                            <input type="checkbox" :id="genre.name" :value="genre.id" v-model="choosenGenres"
                                value="genre.name" class="genre-checkbox">
                            <label :for="genre.name">{{ genre.name }}</label>
                        </div>
                    </div>
                </div>
                <input type="button" name="previous" class="previous action-button" value="Previous" />
                <input type="button" name="next" class="next action-button" value="Next" />
            </fieldset>
            <fieldset>
                <h2 class="fs-title">Welcome!!</h2>
                <h3 class="fs-subtitle">가입을 환영합니다.</h3>
                <input type="button" name="previous" class="previous action-button" value="Previous" />
                <input type="submit" name="submit" class="submit action-button" value="submit" />
            </fieldset>
        </form>
    </div>
</template>
  
<script setup>
import $ from 'jquery'
import 'jquery.easing'
import { ref, onMounted } from 'vue'
import { useMemberStore } from '@/stores/member'
import { useMovieStore } from '@/stores/movie'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const memberStore = useMemberStore()
const movieStore = useMovieStore()
const choosenGenres = ref([])

const signup = function () {
    const payload = {
        username: username.value,
        password1: password1.value,
        password2: password2.value,
        nickname: nickname.value,
        like_genre: choosenGenres.value
    }
    memberStore.signup(payload)
}

onMounted(() => {
    movieStore.getGenres()
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
.genre-checkbox {
    margin-right: 10px;
}

.genre-checkboxes {
    display: flex;
    flex-direction: row;
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
  