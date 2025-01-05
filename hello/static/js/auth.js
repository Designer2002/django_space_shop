document.addEventListener("DOMContentLoaded", () => {
    const loginModal = document.getElementById("login-modal");
    const registerModal = document.getElementById("register-modal");

    const loginBtn = document.getElementById("loginlogin");
    const loginCartBtn = document.getElementById("logincart");
    const openLoginBtns = [loginBtn, loginCartBtn]
    const openLoginBtn2 = document.getElementById("login2");
    const openRegisterBtn = document.getElementById("register");
    console.log(openLoginBtns)

    const closeLoginBtn = document.getElementById("close-login");
    const closeRegisterBtn = document.getElementById("close-register");
    const regform = document.getElementById('regform')
    const logform = document.getElementById('logform')
    const logoutform = document.querySelectorAll('#logout')
    const wrong = document.getElementById('wrong')
    if (wrong !== null) {
        console.log("Элемент 'wrong' найден");
        wrong.style.cssText = "margin-top: 10px; margin-bottom: 5px; color: rgb(255, 106, 198); display: none !important;";
    } else {
        console.log("Элемент 'wrong' не найден");
    }
    const wrong2 = document.getElementById('wrong2')
    if (wrong2 !== null)
        wrong2.style = "margin-top: 10px;margin-bottom: 5px;color:rgb(255, 106, 198);display: none !important;"

//    const isAuthenticated ="{{ user.is_authenticated }}";
//
//    // Если пользователь не аутентифицирован, открываем модальное окно
//    if (!isAuthenticated) {
//        loginModal.style.display = "flex";
//        };

    if (logoutform !== null)
    {
        logoutform.forEach((l) => {


        l.addEventListener('submit', (event) => {

            event.preventDefault(); // Останавливаем стандартное поведение формы
            // Получаем данные формы
            const formData = new FormData(l);

            // Отправляем данные формы с помощью Fetch API


            fetch(l.action, {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {

                    console.log(data.redirect_url)
                    window.location.href = data.redirect_url;
                } else {
                    console.log("ERROR")
                }
            })
            .catch(error => {

                console.log(error);

            });
        });
        });
    }


    logform.addEventListener('submit', (event) => {
        event.preventDefault(); // Останавливаем стандартное поведение формы
        // Получаем данные формы
        const formData = new FormData(logform);
    
        // Отправляем данные формы с помощью Fetch API


        fetch(logform.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect_url;
            } else {
                if (wrong !== null)
                    wrong.style.display = "block";
            }
        })
        .catch(error => {
            if (wrong !== null)
            {
                wrong.textContent = "A network error has occured.";
                wrong.style.display = "block";
            }
            console.log(error);
            
        });
    });


    // Функция для получения CSRF-токена из cookie
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
    }


    openLoginBtns.forEach((openLoginBtn) =>
    {
        openLoginBtn.addEventListener("click", () => {

            if(loginModal.style.display == "flex")
            {
                loginModal.style.display = "none";
            }
                loginModal.style.display = "flex";

        });
    });

    openLoginBtn2.addEventListener("click", () => {
        if(registerModal.style.display == "flex")
        {
            registerModal.style.display = "none";
        }
            loginModal.style.display = "flex";
    });

    openRegisterBtn.addEventListener("click", () => {
        if(loginModal.style.display == "flex")
            {
                loginModal.style.display = "none";
            }
                registerModal.style.display = "flex";
                
    });

    closeLoginBtn.addEventListener("click", () => {
        loginModal.style.display = "none";
    });

    closeRegisterBtn.addEventListener("click", () => {
        registerModal.style.display = "none";
    });

    // Close modals when clicking outside
    window.addEventListener("click", (event) => {
        if (event.target === loginModal) {
            loginModal.style.display = "none";
        }
        if (event.target === registerModal) {
            registerModal.style.display = "none";
        }
    });

    regform.addEventListener('submit', (event) => {
        event.preventDefault();
        const formData = new FormData(regform);
    
        fetch(regform.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || "Registration failed");
                });
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect_url;
            }
        })
        .catch(error => {
            if (wrong2 !== null)
            wrong2.style.display = "block";
            console.error("Registration error:", error);
        });
    });


});
