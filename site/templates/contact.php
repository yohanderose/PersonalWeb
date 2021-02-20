<!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <meta name="author" content="yohan">

      <title>yohan | contact</title>

      <?php include "./assets/includes.html" ?>

</head>
<body>
      <div class="wrapper">

            <?php include "./assets/nav.html" ?>

            <div class="whitespace"></div>

            <!--------------- hero section starts here --------------->
            <div class="container">
                  <div class="hero-content">
                        <br><br>

                        <div class="row">
                              <div class="col-lg-8">

                                    <h3 class="wow fadeInUp" data-wow-delay=".2s">contact &#9996;&#127998;</h3><br>
                                    <p class="wow fadeInUp" data-wow-delay=".2s">Working on something moist? Let me in.</p>

                              </div>
                        </div>
                  </div>
            </div>
            <!--------------- hero section ends here --------------->

            <!-- <div class="whitespace"></div> -->

            <!--------------- form section starts here --------------->
            <div class="container-fluid">
                  <div class="row">
                        <div class="col-lg-8">
                              <form name="contact-form" id="contact-form" method="post" action="">

                              <ul>

                              <li class="wow fadeInUp" data-wow-delay="0.4s">
                                    <label for="contact-name">Name :</label>
                                    <div class="textarea">
                                          <input type="text" name="contact-name" id="contact-name" value="" required>
                                    </div>
                              </li>

                              <li class="wow fadeInUp" data-wow-delay="0.6s">
                                    <label for="contact-email">Email :</label>
                                    <div class="textarea">
                                          <input type="email" name="contact-email" id="contact-email" value="" required>
                                    </div>
                              </li>

                              <li class="wow fadeInUp" data-wow-delay="0.6s">
                                    <label for="contact-project">Message :</label>
                                    <div class="textarea">
                                          <textarea type="email" name="contact-project" id="contact-project" rows="6" value="" required>
                                          </textarea>
                                    </div>
                              </li>

                              </ul>

                              <button type="submit" name="contact-submit" id="contact-submit" class="send wow fadeInUp">Send Message</button>

                              </form>
                        </div>
                  </div>
            </div>

            <!--------------- form section ends here --------------->

            <div class="whitespace"></div>

            <?php include "./assets/footer.html" ?>

            <br><br>

      </div>

      <?php include "./assets/animation.html" ?>
</body>
</html>
