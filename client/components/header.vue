<template>
    <header class="mt-2 mb-5 px-0 d-flex justify-content-center">
        <div class="row container">
            <div class="col col-md-2 px-0">
                <img src="images/header-logo.svg"/>
            </div>
            <div class="col col-md-8 px-0 d-flex justify-content-center align-items-end">
                <div class="row container-fluid justify-content-start align-items-center nav-links">
                    <div class="col col-md-2 px-0 ml-1">
                        <a href="#" class="profession-link text-slate d-flex align-items-center">
                            <i data-feather="align-justify" class="ml-1"></i>
                            لیست تخصص ها
                        </a>
                    </div>
                    <div class="col col-md-2 px-0 ml-1">
                        <a href="#" class=" consultant-link text-slate d-flex align-items-center">
                            <i data-feather="wifi" class="ml-1"></i>
                            مشاوره آنلاین
                        </a>
                    </div>
                    <div class="col col-md-2 px-0 ml-1">
                        <a href="#" class="text-slate d-flex align-items-center">
                            <i data-feather="book" class="ml-1"></i>
                            مجله پزشکی
                        </a>
                    </div>
                    <div class="col col-md-2 px-0 ml-1">
                        <a href="#" class="text-slate d-flex align-items-center">
                            <i data-feather="user-plus" class="ml-1"></i>
                            عضویت پزشکان
                        </a>
                    </div>
                    <div class="col col-md-2 px-0 ml-1">
                        <a href="#" class="text-slate d-flex justify-content-center align-items-center">
                            <i data-feather="box" class="ml-1"></i>
                            کرونا سازمانی
                        </a>
                    </div>
                </div>

            <div class="header-profession-block">
                <div class="overlay">
                </div>
                <div class="modal">
                    sina
                </div>
            </div>

            <div class="header-consultant-block">
                <div class="overlay">
                </div>
                <div class="modal">
                    sina
                </div>
            </div>



            </div>
            <div class="col col-md-2 px-0 d-flex justify-content-end align-items-center">
                <nuxt-link to="/login" class="d-flex align-items-center px-3 py-1 rounded login-button" style="text-decoration: none">
                    <span class="ml-1">ورود</span>
                    <i class="flip-horizontal" data-feather="log-in"></i>
                </nuxt-link>
            </div>
        </div>
    </header>
</template>