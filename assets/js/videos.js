
<script type="text/javascript" src="index.js"></script>


<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>

<script>
        AOS.init();

    </script>
<script type="text/javascript">
        window.addEventListener("scroll", function() {
            var header = document.querySelector("header");
            header.classList.toggle("sticky", window.scrollY > 0);
        })

    </script>
<script>
        function openNav() {
            document.getElementById("myNav").style.width = "100%";
        }

        function closeNav() {
            document.getElementById("myNav").style.width = "0%";
        }

    </script>
<script src="{% static 'js/swiper-bundle.js' %}"></script>
<script src="{% static 'js/swiper-bundle.min.js' %}"></script>
<script>
        var swiper = new Swiper('.swiper-container', {
            speed: 600,
            parallax: true,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });

    </script>