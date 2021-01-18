<template>
    <main class="container mb-5 px-0">
        <div class="row mb-4">
            <nav class="nav">
              <a class="nav-link px-0 d-flex align-items-center active" href="#">درمانکده <i data-feather="chevron-left"></i></a>
              <a class="nav-link px-0 disabled" href="#" tabindex="-1" aria-disabled="true">متخصص مغز و اعصاب (نورولوژی)</a>
            </nav>
        </div>
        <div class="row p-3 mb-4" style="background-color: #1780df;border-radius: 10px">
            <h1 class="text-white font-weight-bold" style="font-size: 28px">
                لیست بهترین متخصص مغز و اعصاب(نورولوژی) برای مشاوره آنلاین و حضوری
            </h1>
            <p class="mb-0  mt-3 mt-md-4 font-14 text-white" data-v-b94103ac="">
                ویزیت حضوری و مشاوره آنلاین (تصویری، صوتی و متنی) با بهترین پزشکان متخصص مغز و اعصاب(نورولوژی) در تهران
            </p>
        </div>

        <!-- ******* -->
        <!-- DOCTORS -->
        <!-- ******* -->

        <div class="row" style="line-height: 26px">
            <div class="col col-md-3 pl-3 pr-0">
                <div class="row container-fluid m-0 p-0 mb-3">
                    <img style="width: 100%" src="images/doctors-slider.png">
                </div>
                <div class="card mb-3 my-card">
                    <div class="card-header text-slate px-3 py-3 text-right my-card-header">
                        <strong>جستجو در نتایج</strong>
                    </div>
                    <div class="card-body">
                        <div class="row align-items-center px-1 py-2">
                            <i data-feather="search" class="text-steel"></i>
                            <input type="text" class="search-input" placeholder="نام یا نام خانوادگی پزشک را بنویسید." />
                        </div>
                    </div>
                </div>
                <div class="card mb-3 my-card">
                    <div class="card-header text-slate d-flex px-3 py-2 text-right my-card-header">
                        <div class="col-md-6 p-0 text-right">
                            <strong class="justify-content-end">تخصص</strong>
                        </div>
                        <div class="col-md-6 p-0 text-left">
                            <i data-feather="chevron-down" class="text-left" style="color: #1780df"></i>
                        </div>
                    </div>
                </div>
                <div class="card mb-3 my-card">
                    <div class="card-header text-slate d-flex px-3 py-2 text-right my-card-header">
                        <div class="col-md-6 p-0 text-right">
                            <strong class="justify-content-end">زمان نوبت</strong>
                        </div>
                        <div class="col-md-6 p-0 text-left">
                            <i data-feather="chevron-down" class="text-left" style="color: #1780df"></i>
                        </div>
                    </div>
                </div>
                <div class="card mb-3 my-card">
                    <div class="card-header text-slate d-flex px-3 py-2 text-right my-card-header">
                        <div class="col-md-6 p-0 text-right">
                            <strong class="justify-content-end">بیمارستان</strong>
                        </div>
                        <div class="col-md-6 p-0 text-left">
                            <i data-feather="chevron-down" class="text-left" style="color: #1780df"></i>
                        </div>
                    </div>
                </div>
                <div class="card mb-3 my-card">
                    <div class="card-header text-slate d-flex px-3 py-2 text-right my-card-header">
                        <div class="col-md-6 p-0 text-right">
                            <strong class="justify-content-end">جنسیت</strong>
                        </div>
                        <div class="col-md-6 p-0 text-left">
                            <i data-feather="chevron-down" class="text-left" style="color: #1780df"></i>
                        </div>
                    </div>
                </div>
                <div class="card mb-3 my-card">
                    <div class="card-header text-slate d-flex px-3 py-2 text-right my-card-header">
                        <div class="col-md-11 p-0 text-right">
                            <strong class="justify-content-end">نمایش پزشکان دارای مشاوره آنلاین</strong>
                        </div>
                        <div class="col-md-1 p-0 text-left">
                            <input type="checkbox">
                        </div>
                    </div>
                </div>
            </div>
            <div class="col col-md-9 pb-3 doctor-items-container">
                <div class="row">
                    <div class="card container-fluid my-card">
                        <div class="row  p-3">
                            <i data-feather="sliders" class="ml-2"></i>
                            <div class="text-slate">
                                <strong>مرتب سازی براساس:</strong>
                            </div>
                            <div class="col-md-6">
                                <div class="row justify-content-around">
                                    <div v-bind:class="{'active-sort px-2 py-1': !sortActive, 'text-steel': sortActive}" @click="reset()">
                                        منتخب
                                    </div>
                                    <div v-bind:class="{'active-sort px-2 py-1': sortActive, 'text-steel': !sortActive}" @click="sort()">
                                        بیشترین رضایتمندی
                                    </div>
                                    <div class="text-steel">
                                        زودترین نوبت
                                    </div>
                                </div>

                            </div>
                        </div>

                    </div>
                </div>
                <nuxt-link class="card row my-3 py-3 px-2 doctor-card" style="text-decoration: none" v-for="doctor in doctors" :key="doctor.node.pk" :to="'/doctor/' + doctor.node.pk">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" :src="doctor.avatar">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">{{ doctor.node.name }}</h5>
                            <p class="text-slate">{{ doctor.node.spec.name }}</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px" v-for="star in doctor.stars" :key="star"></i>
                                    <p class="text-steel" style="font-size: 12px">({{ doctor.comments }} نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>{{ doctor.comment_text }}</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">{{ doctor.node.address }}</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری {{ doctor.node.experienceYears }} سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">{{ doctor.user_percent }} درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <div v-html="heartSVG" class="favorite-icon"></div>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی {{ doctor.first_empty_date }}</p>
                            </div>
                        </div>
                    </div>
                </nuxt-link>
                <!-- <div class="card row my-3 py-3 px-2 doctor-card">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" src="https://www.darmankade.com/UploadFiles/Doctor/131899428573066339دکتر-مهران-جلالی.jpg">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">مهران جلالی</h5>
                            <p class="text-slate">متخصص مغز و اعصاب (نورولوژی)</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <p class="text-steel" style="font-size: 12px">(۵۲ نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>“ آقای دکتر خیلی با صبر وحوصله با بیمار برخورد میکنه. از نظر من عالی هستن😊 “</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">تهران | پونک</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری ۲۷ سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">۹۴ درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <i data-feather="heart" class="favorite-icon"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی سه شنبه ۲ دی</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card row my-3 py-3 px-2 doctor-card">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" src="https://www.darmankade.com/UploadFiles/Doctor/131899428573066339دکتر-مهران-جلالی.jpg">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">مهران جلالی</h5>
                            <p class="text-slate">متخصص مغز و اعصاب (نورولوژی)</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <p class="text-steel" style="font-size: 12px">(۵۲ نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>“ آقای دکتر خیلی با صبر وحوصله با بیمار برخورد میکنه. از نظر من عالی هستن😊 “</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">تهران | پونک</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری ۲۷ سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">۹۴ درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <i data-feather="heart" class="favorite-icon"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی سه شنبه ۲ دی</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card row my-3 py-3 px-2 doctor-card">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" src="https://www.darmankade.com/UploadFiles/Doctor/131899428573066339دکتر-مهران-جلالی.jpg">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">مهران جلالی</h5>
                            <p class="text-slate">متخصص مغز و اعصاب (نورولوژی)</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <p class="text-steel" style="font-size: 12px">(۵۲ نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>“ آقای دکتر خیلی با صبر وحوصله با بیمار برخورد میکنه. از نظر من عالی هستن😊 “</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">تهران | پونک</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری ۲۷ سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">۹۴ درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <i data-feather="heart" class="favorite-icon"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی سه شنبه ۲ دی</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card row my-3 py-3 px-2 doctor-card">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" src="https://www.darmankade.com/UploadFiles/Doctor/131899428573066339دکتر-مهران-جلالی.jpg">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">مهران جلالی</h5>
                            <p class="text-slate">متخصص مغز و اعصاب (نورولوژی)</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <p class="text-steel" style="font-size: 12px">(۵۲ نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>“ آقای دکتر خیلی با صبر وحوصله با بیمار برخورد میکنه. از نظر من عالی هستن😊 “</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">تهران | پونک</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری ۲۷ سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">۹۴ درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <i data-feather="heart" class="favorite-icon"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی سه شنبه ۲ دی</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card row my-3 py-3 px-2 doctor-card">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" src="https://www.darmankade.com/UploadFiles/Doctor/131899428573066339دکتر-مهران-جلالی.jpg">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">مهران جلالی</h5>
                            <p class="text-slate">متخصص مغز و اعصاب (نورولوژی)</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <p class="text-steel" style="font-size: 12px">(۵۲ نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>“ آقای دکتر خیلی با صبر وحوصله با بیمار برخورد میکنه. از نظر من عالی هستن😊 “</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">تهران | پونک</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری ۲۷ سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">۹۴ درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <i data-feather="heart" class="favorite-icon"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی سه شنبه ۲ دی</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card row my-3 py-3 px-2 doctor-card">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" src="https://www.darmankade.com/UploadFiles/Doctor/131899428573066339دکتر-مهران-جلالی.jpg">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">مهران جلالی</h5>
                            <p class="text-slate">متخصص مغز و اعصاب (نورولوژی)</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <p class="text-steel" style="font-size: 12px">(۵۲ نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>“ آقای دکتر خیلی با صبر وحوصله با بیمار برخورد میکنه. از نظر من عالی هستن😊 “</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">تهران | پونک</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری ۲۷ سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">۹۴ درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <i data-feather="heart" class="favorite-icon"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی سه شنبه ۲ دی</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card row my-3 py-3 px-2 doctor-card">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" src="https://www.darmankade.com/UploadFiles/Doctor/131899428573066339دکتر-مهران-جلالی.jpg">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">مهران جلالی</h5>
                            <p class="text-slate">متخصص مغز و اعصاب (نورولوژی)</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <p class="text-steel" style="font-size: 12px">(۵۲ نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>“ آقای دکتر خیلی با صبر وحوصله با بیمار برخورد میکنه. از نظر من عالی هستن😊 “</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">تهران | پونک</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری ۲۷ سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">۹۴ درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <i data-feather="heart" class="favorite-icon"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی سه شنبه ۲ دی</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card row my-3 py-3 px-2 doctor-card">
                    <div class="row container-fluid p-0 m-0">
                        <div class="col-md-2">
                            <img style="width: 100%" src="https://www.darmankade.com/UploadFiles/Doctor/131899428573066339دکتر-مهران-جلالی.jpg">
                        </div>
                        <div class="col-md-5 py-2">
                            <h5 class="text-slate">مهران جلالی</h5>
                            <p class="text-slate">متخصص مغز و اعصاب (نورولوژی)</p>
                            <div class="row">
                                <div class="col-md-6 d-flex justify-content-around">
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <i data-feather="star" style="color: #1780df;fill: #1780df;width: 14px"></i>
                                    <p class="text-steel" style="font-size: 12px">(۵۲ نظر)</p>
                                </div>
                            </div>
                            <div class="row text-steel">
                                <p>“ آقای دکتر خیلی با صبر وحوصله با بیمار برخورد میکنه. از نظر من عالی هستن😊 “</p>
                            </div>

                        </div>
                        <div class="col-md-5 py-2">
                            <div class="doctor-address-container text-steel p-2">
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="map-pin"></i>
                                    <p class="px-2 m-0">تهران | پونک</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="book"></i>
                                    <p class="px-2 m-0">تجربه کاری ۲۷ سال</p>
                                </div>
                                <div class="row container-fluid align-items-center py-1">
                                    <i data-feather="thumbs-up"></i>
                                    <p class="px-2 m-0">۹۴ درصد رضایت کاربران</p>
                                </div>
                            </div>
                            <div class="row container-fluid p-0 my-2 mx-0">
                                <div class="col-md-10 p-0 pl-4 m-0">
                                    <button class="btn btn-block my-button px-2 py-3">
                                        <div class="row align-items-center">
                                            <div class="col-md-3 d-flex justify-content-center align-items-center p-0">
                                                <i data-feather="arrow-left"></i>
                                            </div>
                                            <div class="col-md-9 d-flex justify-content-center align-items-center p-0">
                                                <p class="m-0">نوبت بگیر!</p>
                                            </div>
                                        </div>
                                        <div class="button-overlay"></div>
                                    </button>
                                </div>
                                <div class="col-md-2 p-0">
                                    <button class="btn btn-block p-0 m-0 favorite-button">
                                        <i data-feather="heart" class="favorite-icon"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center">
                                <p style="color: #4dcc6b" class="font-14 mb-0">اولین نوبت خالی سه شنبه ۲ دی</p>
                            </div>
                        </div>
                    </div>
                </div> -->
            </div>
        </div>

        <!-- ******* -->
        <!-- DOCTORS -->
        <!-- ******* -->



        <!-- *********** -->
        <!-- INFORMATION -->
        <!-- *********** -->

        <div class="row card my-card my-3 p-3 border-0" style="background-color: #e5f2fe">
            <h4 class="text-slate">هر آنچه که باید از <span style="color: #1780df">متخصص مغز و اعصاب(نورولوژی)</span>بدانید!</h4>
            <p class="text-steel my-3">سیستم عصبی انسان به دو دسته‌ی کلی اعصاب مرکزی (مغز و نخاع) و اعصاب محیطی (اعصاب و نورون‌های عضلات) تقسیم می‌شود. تمام بیماری‌هایی که هر یک از این قسمت‌ها را درگیر کند، توسط پزشک متخصص مغز و اعصاب درمان می‌شوند.</p>
            <p class="text-steel"><strong>پزشک مغز و اعصاب </strong>بیماریهایی از قبیل انواع سرد</p>
            <div class="row px-3 justify-content-end">
                <button class="d-flex justify-content-around align-items-center py-1 my-button">
                    <p class="m-0">بیشتر بخوانید</p>
                    <i data-feather="chevron-down"></i>
                </button>
            </div>
        </div>

        <!-- *********** -->
        <!-- INFORMATION -->
        <!-- *********** -->


        <!-- *** -->
        <!-- FAQ -->
        <!-- *** -->

        <div class="row card my-card p-3">
            <h5 class="text-slate mb-5"><strong>متخصص مغز و اعصاب(نورولوژی)</strong></h5>

            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
            <div class="row container-fluid mx-auto my-3 pb-3" style="border-bottom: 1px solid #dee2e6">
                <i data-feather="plus" style="color: white;background-color: rgb(23, 128, 223);border-radius: 25% 0 25% 25%;padding: 3px"></i>
                <h5 class="font-14 m-0 align-self-end mr-2 text-slate">⭐بیماران چه زمانی باید به متخصص مغز و اعصاب یا جراح مغز و اعصاب و یا به روانپزشک مراجعه کنند؟</h5>
            </div>
        </div>

        <!-- *** -->
        <!-- FAQ -->
        <!-- *** -->


    </main>

</template>
<script>
import feather from 'feather-icons'

export default {
    layout: 'pages',
    data() {
        return {
            doctors: [],
            sortActive: false
        }
    },
    created: function(){
        this.init()
    },
    methods: {
        init: function(){
            this.$apollo.query({
                query: require('../graphql/doctors.gql'),
                variables: {
                    spec: this.$route.query.spec,
                    name: this.$route.query.name
                }
            }).then(data => {
                this.doctors = data.data.doctors.edges
            })
        },
        sort: function(){
            this.sortActive = true
            debugger
            this.doctors.sort((first, second) => {
                return (first.user_percent > second.user_percent)?-1:(first.user_percent < second.user_percent)?1:0
            })
        },
        reset: function(){
            this.sortActive = false
            this.init()
        }
    },
    computed: {
        heartSVG: function(){
            return feather.toSvg('heart')
        }
    }
}
</script>
<style scoped>
    @import url('@/assets/doctors.css');
    .active-sort {
        color: white;
        background-color: #1780df;
        border-radius: 10px
    }
</style>