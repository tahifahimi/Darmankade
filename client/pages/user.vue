<template>
    <div class="container">
        <div v-if="success" style="color: green">اطلاعات ویرایش شد</div>
        <div>
            <h2>اطلاعات فردی:</h2>
            <br />
            <label>نام کاربری: </label>
            <input class="my-1" type="text" v-model="user.username" placeholder="نام کاربری" disabled>
            <br />
            <label>نام: </label>
            <input class="my-1" type="text" v-model="user.firstName" placeholder="نام">
            <br />
            <label>نام خانوادگی: </label>
            <input class="my-1" type="text" v-model="user.lastName" placeholder="نام خانوادگی">
            <br />
            <label> موبایل: </label>
            <input class="my-1" type="text" v-model="user.mobile" placeholder="موبایل">
            <br />
            <label>رمز عبور: </label>
            <input class="my-1" type="text" v-model="user.password" placeholder="رمز عبور">
            <br />
        </div>
        <br />
        <br />
        <br />
        <div v-if="user.type==='doctor'">
            <h2>اطلاعات پزشکی:</h2>
            <br />
            <label> تخصص: </label>
            <select v-model="user.doctor.spec">
                <option v-for="spec in specs" :key="spec.id" :value="spec">{{ spec.name }}</option>
            </select>
            <br />
            <label> شماره نظام پزشکی: </label>
            <input class="my-1" type="text" v-model="user.doctor.number">
            <br />
            <label>پرداخت آنلاین: </label>
            <input class="my-1" type="checkbox" v-model="user.doctor.onlinePay">
            <br />
            <label> تجربه:‌</label>
            <input class="my-1" type="text" v-model="user.doctor.experienceYears">
            <br />
            <label>آدرس: </label>
            <textarea v-model="user.doctor.address" />
            <br />
            <label>تلفن مطب: </label>
            <input class="my-1" type="text" v-model="user.doctor.phone">
            <br />
            <span v-for="(value, index) in days" :key="index">
                <label>{{ value }}</label>
                <input class="my-1" type="checkbox" v-model="user.doctor.weekDays[index]" />
                <br />
            </span>
        </div>
        <button class="btn btn-primary" @click="submit">ثبت</button>
    </div>
</template>

<script>
export default {
    layout: 'login',
    data() {
        return {
            user: {},
            specs:[],
            days: [
                'شنبه',
                'یکشنبه',
                'دوشنبه',
                'سه شنبه',
                'چهارشنبه',
                'پنج شنبه',
                'جمعه',
            ],
            success: false
        }
    },
    created: function(){
        this.$apollo.query({
            query: require('../graphql/user.gql')
        }).then(data => {
            this.user = data.data.user
            this.user.password = ""
        }).catch(error => {
            this.$router.push('/login')
        })
        this.$apollo.query({
            query: require('../graphql/specs.gql')
        }).then(data => {
            this.specs = data.data.specs
        }).catch(error => {
            console.log(error)
        })
    },
    methods: {
        submit: function(){
            console.log(this.user)
            let doctor = null
            if(this.user.type === "doctor"){
                doctor = {
                            id: this.user.doctor.id,
                            number: this.user.doctor.number,
                            onlinePay: this.user.doctor.onlinePay,
                            experienceYears: this.user.doctor.experienceYears,
                            address: this.user.doctor.address,
                            phone: this.user.doctor.phone,
                            weekDays: this.convert(this.user.doctor.weekDays),
                            spec: this.user.doctor.spec.id
                        }
            }
            let data = {
                id: this.user.id,
                firstName: this.user.firstName,
                lastName: this.user.lastName,
                mobile: this.user.mobile,
                type: "client",
                doctor: doctor,
                username: this.user.username,
                password: this.user.password
            }
            console.log(data)
            this.$apollo.mutate({
                mutation: require('../graphql/userMutation.gql'),
                variables: {
                    input: data
                }
            }).then(data => {
                if(data.data.userMutation.errors)
                    throw(data.data.userMutation.errors)
                this.success = true
            }).catch(error => {
                console.log(error)
            })
        },
        convert: function(list){
            let result = ""
            for(let day in list)
                if(list[day])
                    result += "T"
                else
                    result += "F"
            return result
        }
    }
}
</script>

<style scoped>
input, select, option {
    border: 2px solid black;
    width: 50%
}
</style>