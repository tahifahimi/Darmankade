<template>
    <div class="login-container">
        <div class="right-hand">
            <img src="images/login-logo.svg" />
            <h2>به درمانکده خوش آمدید</h2>
            <h5>نوبت دهی آنلاین مطب پزشکان</h5>
        </div>
        <div class="left-hand">
            <h4>ورود</h4>
            <fieldset class="mobile-fieldset">
                <legend>نام کاربری</legend>
                <input type="text" v-model="info.username" placeholder="مثلا test"/>
            </fieldset> 
            <fieldset class="mobile-fieldset">
                <legend>کلمه عبور</legend>
                <input type="password" v-model="info.password" placeholder="مثلا 12345"/>
            </fieldset> 
            <button @click="login" class="login-button">
                <span>ورود</span>
                <i data-feather="chevrons-left"></i>
            </button>
            <button class="moaref">
                کد معرف دارید؟
            </button>
            <a href="#">
                <div>
                    <img class="google-logo" src="images/google.png" />
                    <br />
                    <span style="color:#1780df;border-bottom: 1px dashed #1780df;padding-bottom: 3px;">ورود با گوگل</span>
                </div>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    layout: 'login',
    data() {
        return {
            info: {
                username: "",
                password: ""
            }
        }
    },
    methods: {
        login: function(){
            this.$apollo.mutate({
                mutation: require('../graphql/login.gql'),
                variables: this.info
            }).then(data => {
                this.$router.push('/user')
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
@import url('@/assets/login.css');
</style>