# Test-Taking-System
Online test taking system with face recognition

Abstract

Nowadays, Online Examination are gaining popularity.
As more and more institutions, schools, colleges and
universities are using this evacuation system to conduct examinations.
There is a growing need in developing solutions which can
support and provide a platform for fair evaluation. The current
solutions are either providing limited functionalities or are rather
too expensive for small education institutions like schools to
consider using in their daily operations. Test Management System
is a web solution which can be used by any educational institution
for conducting exams. This system will help them to conduct
an online exam by continuously monitoring participants during
exam. By using face recognition, face detection, and mouse cursor
monitoring it creates a controlled environment for participants
to take part in a fair evaluation. Result of this intense participant
monitoring can work as a perfect tool for preventing plagiarism
and cheating during exam.
Index Terms—Introduction, RelatedWorks, Proposed Solution,
Limitations, Conclusion and Future Work, References

I. INTRODUCTION
As the pandemic continuous, the need of online solutions in
the education system is on a rise.[1] To continue the working
of educational institution, new product and technologies are
applied to make online education more effective. Student
evaluation is a major part of academics. Though there are
various solution which are similar and conduct exams in a
seamless manner. They fail to address issues like plagiarism
and cheating effectively. We will discuss about some of
related projects in the upcoming section. To address these
issues and create an evaluation system that can effectively
conduct fair evaluation. The Test Management System uses
face recognition, face detection and mouser cursor tracking to
monitor participant during examination. Also, physical exams
need various resources and facilities (lights, sitting, and others)
to conduct evaluation. The web solution Test Management
system is inexpensive and makes organizing evaluation easy.
By providing secure access to exam, it prevents any one user
from getting an unfair advantage over the others. The web
application makes use of face recognition API python which
provides 99.3 percent accuracy results [5]. A notification is
sent to the exam organizer if there is a case of plagiarism.

II. RELATED WORKS
There are various projects that provide different features
and have varied level of user experiences. There are also
some research projects that focus on Online evaluation system.
Web-based Exam Management System introduced by Rashad
Et. Al. (2010) is a solution that is intended to provide easy
evaluation in the case when the number of participants are
larger. In that case it is infeasible to evaluate all the participants
by conventional methods of manually checking answer. This
paper on Web Based Examination proposes an Auto-grading
functionality. It has support for many kinds of question.
The web-based approach makes it easy for them to conduct
evaluation on both local and remote environment. Though this
paper answers to the requirements on feasibility it does not
address plagiarism and cheat. The evaluation is meaningful if
all the participants are competing in the same environment and
without any unfair advantage. [2]
Development of Online Examination Platform for Better
Evaluation and Monitoring by Agam Garg1, Anuj Jaiswal2,
Anushka Gupta3, Diksha Tripathi4 is an online based approach
to evaluation. There participants can login and give their exam
in a specific time limit. These tests are customizable and
provides feasibility to generating exams. Though it provides
secure login with help of questioner verification, it still does
not answer to a case when the answer to those questions is
shared or the credentials of login are shared with another
person. [3]
Computer-Based Test (Cbt) System for University Academic
Enterprise Examination by Fagbola Temitayo M., Adigun
Adebisi A., Oke Alice O. is a flexible approach to mass
scale evaluation. The system is designed to create a more automated
approach to evaluation where the submission, checking
and report generation are done automatically reducing the
work for organizers. This solution provides reliability and
easy to use environment which helps in conducting evaluation
for much larger audiences. Though it relies only on time
base approach for providing fair evolution. This makes this
approach vulnerable to cases of plagiarism. It also does not
address the concept that some evaluations are much more
dependent on quality of answer then the speed at which the
evaluation is completed. [4]

III. PROPOSED SOLUTION
The Test Management System makes use of various technologies
to prevent cheating, plagiarism and someone to pose
as the participant during examination. It achieves this using
face verification to determine the identity of participant. The
face verification provides accuracy of about 99.3 precent
[5]. This makes verification process accurate and prevents
from unauthorized access to test platform. The web-based
solution provides user friendly access to quiz, registration and
report after test quiz is complete. This system is capable of
creating and conducting a variety evaluation as per the course
requirements. It makes use of face detection during the quiz
session to prevent the user from plagiarism by monitoring their
movement during exam. Mouse cursor moment is monitored
and recorded to prevent user from switching tabs or engaging
in other activities during evaluation. Introducing these features
makes evaluation system secure and prevent cheating.

A. Application Architecture
Fig. 1. Application Architecture Overview
The application architecture uses the Django framework.
The request is sent to url.py which routes the request to the
specific view depending on url and request type. View then
creates a dynamic response to the user’s request. This response
is generated using templates, models, face recognition api, and
other back-end packages. The response which consists of user
specific data is then forwarded to the user. Face recognition,
face detection, and mouse cursor monitoring are part of view
and template. On the bases of request, database operation can
be triggered.

B. Face Recognition
During the registration process, the user provides their
photo. This photo is then used to identify the user. When
user login using their credentials, they are redirected to a
page which requires access to the webcam. The user then
takes a photo such that their face is visible. This photo is
then sent to sever. The face is recognized using the Face
Recognition API. This API has a pre-trained model and we
configure this model to identify a match between user’s profile
picture and their identification picture which was just received
during verification. If the match is about the threshold limit,
the user is redirected to the profile page. This process makes
sure that only the person whose profile it is can only access
their content. Face recognition is used to of identifying or
verifying the identity of an individual using their face. There
are various machine learning algorithms and models which can
achieve this with varying degree of accuracy. Face recognition
API uses deep learning algorithms for recognition. The face
recognition library developed by Adam Geitgey uses dlib’s
facial recognition features. Dlib by Davis King consists of
the implementation of matric-based deep learning which is
used for face embeddings that then facilitates the recognition
process.

C. Face Detection
During the quiz, the participant is monitored using
face detection. This is achieved with JavaScript Face-API.
Participants are only allowed to concentrate on evaluation.
This prevents users from locking around for book content,
searching answers on the web using their phone, or any other
activity. The participants therefore only answer the questions
based on their knowledge. This facilitates a fair examination,
which can potentially improve the credibility of the course
itself. The Face API JS is built on TensorFlow to provide
face detection. It identifies a face using the Convolutional
Neural Network model. This model 68-point face landmarks
for a successful face fond on the image. The application
makes sure that only one user is participating in answering
questions. This prevents the user from taking external help
during evaluation, therefore preventing cheating. In case the
student tries to cheat during exam. A notification will be sent
to organizer that the student is suspected for cheating.

D. Mouse Cursor Monitoring
While the participant is taking their quiz, they are required
to keep their cursor on the exam sheet. This feature is
implemented using JavaScript. If the user tries to change
their tab or go out of the scope of paper during exam. A
notification is sent to the teacher about irregularity in cursor.
This feature prevents the user form engaging in searching for
solution of web using that same machine on which the exam is
proceeding. The Notification first tries to notify the user about
keeping their cursor in designated scope. If the irregularity
continues for a considerable amount of time, then teacher is
notified.
The mouse event element has parameters about position of
cursor on a x and y coordinate bases. Float pixel values are
returned to provide positioning. In this case x is the horizontal
positioning and y is vertical positioning.[8] Theses positional
parameters are monitored for the confined space of quiz
sheet. All the quiz relational functionalities are limited to this
area. Once the cursor moves out of scope a timer is initiate
to check how long the user has been out of section once the
threshold is reached a notification is sent to the user informing
them that during evaluation cursor need to be inside quiz
sheet. If this behavior continues notification is send to teacher.

E. Tools and Technology
During the implementation of Test Management System,
we used various tools and technologies. For front-end HTML,
CSS, Javascript, Bootstrap and Jquery were used. While as
back-end Python, OpenCV and Face Recognition API were
utilized. The web- application uses Django framework.

IV. LIMITATIONS
Though Test Management System is implementing various
key features for conducting monitored exam. There are still
some drawbacks to this solation. Graphical user interface
can be improved to provide more user-friendly experience.
Instruction page and tutorial can make navigation easier for
Fig. 6. Quiz sheet border appear when mouse cursor is outside
first time users. On the other hand, Face recognition can be
improved to provide fast response. Currently, this web solution
only provides support for multiple chose questions and T/F
questions. By introduction more question type flexibility can
be improved in future iterations.

V. CONCLUSION AND FUTURE WORK
In conclusion, we were able to create a web solution that
helps in conducting monitored exams. Using features like face
verification and face detection it can regulate cheating and
plagiarism. It also monitors cursor movement during exam to
prevent the participant from switching tabs or referring other
content. It is capable of creating a quiz and conducting exams
for verified users. Test Management System provides various
functionalities for monitoring and managing evaluation. There
is still scope for future development. Some of possible further
developments are:
 The model for other type of users can be created to
provide more functionalities
 Notification system can be improved to facilitate email
notification.
 More innovative solutions like voice detection can be
added to make Test Management System more secure.

REFERENCES
[1] “Online school will still be around postpandemic,
so what have we learned? — CBC
News,” CBCnews, 15-Mar-2021. [Online]. Available:
https://www.cbc.ca/news/canada/ontario-online-virtual-school-
1.5944407. [Accessed: 01-Apr-2021].
[2] Magdi Z. Rashad, Mahmoud S. Kandil, hmed E.
Hassan, and and Mahmoud A. Zaher, “An Arabic Web-Based
Exam Management System,” Feb. 2010.
[3] Agam Garg, Anuj Jaiswal, Anushka Gupta, and Diksha
Tripathi, “Development of Online Examination Platform for
Better Evaluation and Monitoring.” May-2020.
[4] M., Fagbola Baale, Adebisi Oke, A. (2013). Computer-
Based Test (CBT) System For University Academic Enterprise
Examination.
[5] “face-recognition,” PyPI. [Online]. Available:
https://pypi.org/project/face-recognition/. [Accessed: 15-
Mar-2021].
[6] B. Guven, “Building a Face Recognizer in
Python,” Medium, 06-Sep-2020. [Online]. Available:
https://towardsdatascience.com/building-a-face-recognizer-inpython-
7fd6630c6340. [Accessed: 20-Mar-2021].
[7] V. M¨uhler, “face-api.js - JavaScript API for Face
Recognition in the Browser with tensorflow.js,” Medium,
23-Oct-2018. [Online]. Available: https://itnext.io/face-apijs-
javascript-api-for-face-recognition-in-the-browser-withtensorflow-
js-bcc2a6c4cf07. [Accessed: 23-Mar-2021].
[8] MDN contributors, “Web technology for
developers,” Web APIs — MDN, Feb-2021.
[Online]. Available: https://developer.mozilla.org/en-
US/docs/Web/API/MouseEvent/pageX. [Accessed: 23-
Mar-2021].
