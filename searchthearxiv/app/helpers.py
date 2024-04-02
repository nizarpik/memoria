import json
from paper import Paper
from requests_html import HTMLSession
from collections import defaultdict

def fetch_abstract(url):
    session = HTMLSession()
    r = session.get(url)
    content = r.html.find("#content-inner", first=True)
    abstract = content.find(".abstract", first=True).text
    return abstract

def avg_score(papers):
    avg_score = sum([p.score for p in papers]) / len(papers)
    return round(avg_score, 2)

def get_matches():
    return {
    "papers": [
        {
            "id": "2209.07589",
            "score": 0.79,
            "title": "PIZZA: A Powerful Image-only Zero-Shot Zero-CAD Approach to 6 DoF Tracking",
            "authors": "Van Nguyen Nguyen, Yuming Du, Yang Xiao, Michael Ramamonjisoa, Vincent Lepetit",
            "abstract": "Estimating the relative pose of a new object without prior knowledge is a hard problem, while it is an ability very much needed in robotics and Augmented Reality. We present a method for tracking the 6D motion of objects in RGB video sequences when neither the training images nor the 3D geometry of the objects are available. In contrast to previous works, our method can therefore consider unknown objects in open world instantly, without requiring any prior information or a specific training phase. We consider two architectures, one based on two frames, and the other relying on a Transformer Encoder, which can exploit an arbitrary number of past frames. We train our architectures using only synthetic renderings with domain randomization. Our results on challenging datasets are on par with previous works that require much more information (training images of the target objects, 3D models, and/or depth data). Our source code is available at https://github.com/nv-nguyen/pizza",
            "year": 2022,
            "month": "Sep",
            "authors_parsed": [
                "Van Nguyen Nguyen",
                "Yuming Du",
                "Yang Xiao",
                "Michael Ramamonjisoa",
                "Vincent Lepetit"
            ]
        },
        {
            "id": "1906.02839",
            "score": 0.77,
            "title": "How to make a pizza: Learning a compositional layer-based GAN model",
            "authors": "Dim P. Papadopoulos, Youssef Tamaazousti, Ferda Ofli, Ingmar Weber, Antonio Torralba",
            "abstract": "A food recipe is an ordered set of instructions for preparing a particular dish. From a visual perspective, every instruction step can be seen as a way to change the visual appearance of the dish by adding extra objects (e.g., adding an ingredient) or changing the appearance of the existing ones (e.g., cooking the dish). In this paper, we aim to teach a machine how to make a pizza by building a generative model that mirrors this step-by-step procedure. To do so, we learn composable module operations which are able to either add or remove a particular ingredient. Each operator is designed as a Generative Adversarial Network (GAN). Given only weak image-level supervision, the operators are trained to generate a visual layer that needs to be added to or removed from the existing image. The proposed model is able to decompose an image into an ordered sequence of layers by applying sequentially in the right order the corresponding removing modules. Experimental results on synthetic and real pizza images demonstrate that our proposed model is able to: (1) segment pizza toppings in a weaklysupervised fashion, (2) remove them by revealing what is occluded underneath them (i.e., inpainting), and (3) infer the ordering of the toppings without any depth ordering supervision. Code, data, and models are available online.",
            "year": 2019,
            "month": "Jun",
            "authors_parsed": [
                "Dim P. Papadopoulos",
                "Youssef Tamaazousti",
                "Ferda Ofli",
                "Ingmar Weber",
                "Antonio Torralba"
            ]
        },
        {
            "id": "2212.00265",
            "score": 0.77,
            "title": "PIZZA: A new benchmark for complex end-to-end task-oriented parsing",
            "authors": "Konstantine Arkoudas, Nicolas Guenon des Mesnards, Melanie Rubino, Sandesh Swamy, Saarthak Khanna, Weiqi Sun, Khan Haidar",
            "abstract": "Much recent work in task-oriented parsing has focused on finding a middle ground between flat slots and intents, which are inexpressive but easy to annotate, and powerful representations such as the lambda calculus, which are expressive but costly to annotate. This paper continues the exploration of task-oriented parsing by introducing a new dataset for parsing pizza and drink orders, whose semantics cannot be captured by flat slots and intents. We perform an extensive evaluation of deep-learning techniques for task-oriented parsing on this dataset, including different flavors of seq2seq systems and RNNGs. The dataset comes in two main versions, one in a recently introduced utterance-level hierarchical notation that we call TOP, and one whose targets are executable representations (EXR). We demonstrate empirically that training the parser to directly generate EXR notation not only solves the problem of entity resolution in one fell swoop and overcomes a number of expressive limitations of TOP notation, but also results in significantly greater parsing accuracy.",
            "year": 2022,
            "month": "Dec",
            "authors_parsed": [
                "Konstantine Arkoudas",
                "Nicolas Guenon des Mesnards",
                "Melanie Rubino",
                "Sandesh Swamy",
                "Saarthak Khanna",
                "Weiqi Sun",
                "Khan Haidar"
            ]
        },
        {
            "id": "2012.02821",
            "score": 0.77,
            "title": "MPG: A Multi-ingredient Pizza Image Generator with Conditional StyleGANs",
            "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
            "abstract": "Multilabel conditional image generation is a challenging problem in computer vision. In this work we propose Multi-ingredient Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing multilabel images. We design MPG based on a state-of-the-art GAN structure called StyleGAN2, in which we develop a new conditioning technique by enforcing intermediate feature maps to learn scalewise label information. Because of the complex nature of the multilabel image generation problem, we also regularize synthetic image by predicting the corresponding ingredients as well as encourage the discriminator to distinguish between matched image and mismatched image. To verify the efficacy of MPG, we test it on Pizza10, which is a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realist pizza images with desired ingredients. The framework can be easily extend to other multilabel image generation scenarios.",
            "year": 2020,
            "month": "Dec",
            "authors_parsed": [
                "Fangda Han",
                "Guoyao Hao",
                "Ricardo Guerrero",
                "Vladimir Pavlovic"
            ]
        },
        {
            "id": "2301.01576",
            "score": 0.76,
            "title": "Robofriend: An Adpative Storytelling Robotic Teddy Bear -- Technical Report",
            "authors": "Ido Glanz, Matan Weksler, Erez Karpas, Tzipi Horowitz-Kraus",
            "abstract": "In this paper we describe Robofriend, a robotic teddy bear for telling stories to young children. Robofriend adapts its behavior to keep the childrens' attention using reinforcement learning.",
            "year": 2023,
            "month": "Jan",
            "authors_parsed": [
                "Ido Glanz",
                "Matan Weksler",
                "Erez Karpas",
                "Tzipi Horowitz-Kraus"
            ]
        },
        {
            "id": "2208.00386",
            "score": 0.76,
            "title": "Robotic Dough Shaping",
            "authors": "Jan Ondras, Di Ni, Xi Deng, Zeqi Gu, Henry Zheng, Tapomayukh Bhattacharjee",
            "abstract": "Robotic manipulation of deformable objects gains great attention due to its wide applications including medical surgery, home assistance, and automatic food preparation. The ability to deform soft objects remains a great challenge for robots due to difficulties in defining the problem mathematically. In this paper, we address the problem of shaping a piece of dough-like deformable material into a 2D target shape presented upfront. We use a 6 degree-of-freedom WidowX-250 Robot Arm equipped with a rolling pin and information collected from an RGB-D camera and a tactile sensor. We present and compare several control policies, including a dough shrinking action, in extensive experiments across three kinds of deformable materials and across three target dough shape sizes, achieving the intersection over union (IoU) of 0.90. Our results show that: i) rolling dough from the highest dough point is more efficient than from the 2D/3D dough centroid; ii) it might be better to stop the roll movement at the current dough boundary as opposed to the target shape outline; iii) the shrink action might be beneficial only if properly tuned with respect to the expand action; and iv) the Play-Doh material is easier to shape to a target shape as compared to Plasticine or Kinetic sand. Video demonstrations of our work are available at https://youtu.be/ZzLMxuITdt4",
            "year": 2022,
            "month": "Jul",
            "authors_parsed": [
                "Jan Ondras",
                "Di Ni",
                "Xi Deng",
                "Zeqi Gu",
                "Henry Zheng",
                "Tapomayukh Bhattacharjee"
            ]
        },
        {
            "id": "2203.05187",
            "score": 0.75,
            "title": "Cluttered Food Grasping with Adaptive Fingers and Synthetic-Data Trained Object Detection",
            "authors": "Avinash Ummadisingu, Kuniyuki Takahashi, Naoki Fukaya",
            "abstract": "The food packaging industry handles an immense variety of food products with wide-ranging shapes and sizes, even within one kind of food. Menus are also diverse and change frequently, making automation of pick-and-place difficult. A popular approach to bin-picking is to first identify each piece of food in the tray by using an instance segmentation method. However, human annotations to train these methods are unreliable and error-prone since foods are packed close together with unclear boundaries and visual similarity making separation of pieces difficult. To address this problem, we propose a method that trains purely on synthetic data and successfully transfers to the real world using sim2real methods by creating datasets of filled food trays using high-quality 3d models of real pieces of food for the training instance segmentation models. Another concern is that foods are easily damaged during grasping. We address this by introducing two additional methods -- a novel adaptive finger mechanism to passively retract when a collision occurs, and a method to filter grasps that are likely to cause damage to neighbouring pieces of food during a grasp. We demonstrate the effectiveness of the proposed method on several kinds of real foods.",
            "year": 2022,
            "month": "Mar",
            "authors_parsed": [
                "Avinash Ummadisingu",
                "Kuniyuki Takahashi",
                "Naoki Fukaya"
            ]
        },
        {
            "id": "2205.03530",
            "score": 0.75,
            "title": "Gigs with Guarantees: Achieving Fair Wage for Food Delivery Workers",
            "authors": "Ashish Nair, Rahul Yadav, Anjali Gupta, Abhijnan Chakraborty, Sayan Ranu, Amitabha Bagchi",
            "abstract": "With the increasing popularity of food delivery platforms, it has become pertinent to look into the working conditions of the 'gig' workers in these platforms, especially providing them fair wages, reasonable working hours, and transparency on work availability. However, any solution to these problems must not degrade customer experience and be cost-effective to ensure that platforms are willing to adopt them. We propose WORK4FOOD, which provides income guarantees to delivery agents, while minimizing platform costs and ensuring customer satisfaction. WORK4FOOD ensures that the income guarantees are met in such a way that it does not lead to increased working hours or degrade environmental impact. To incorporate these objectives, WORK4FOOD balances supply and demand by controlling the number of agents in the system and providing dynamic payment guarantees to agents based on factors such as agent location, ratings, etc. We evaluate WORK4FOOD on a real-world dataset from a leading food delivery platform and establish its advantages over the state of the art in terms of the multi-dimensional objectives at hand.",
            "year": 2022,
            "month": "May",
            "authors_parsed": [
                "Ashish Nair",
                "Rahul Yadav",
                "Anjali Gupta",
                "Abhijnan Chakraborty",
                "Sayan Ranu",
                "Amitabha Bagchi"
            ]
        },
        {
            "id": "2110.11830",
            "score": 0.75,
            "title": "Multi-attribute Pizza Generator: Cross-domain Attribute Control with Conditional StyleGAN",
            "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
            "abstract": "Multi-attribute conditional image generation is a challenging problem in computervision. We propose Multi-attribute Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing images from a trichotomy of attributes: content, view-geometry, and implicit visual style. We design MPG by extending the state-of-the-art StyleGAN2, using a new conditioning technique that guides the intermediate feature maps to learn multi-scale multi-attribute entangled representationsof controlling attributes. Because of the complex nature of the multi-attribute image generation problem, we regularize the image generation by predicting the explicit conditioning attributes (ingredients and view). To synthesize a pizza image with view attributesoutside the range of natural training images, we design a CGI pizza dataset PizzaView using 3D pizza models and employ it to train a view attribute regressor to regularize the generation process, bridging the real and CGI training datasets. To verify the efficacy of MPG, we test it on Pizza10, a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realistic pizza images with desired ingredients and view attributes, beyond the range of those observed in real-world training data.",
            "year": 2021,
            "month": "Oct",
            "authors_parsed": [
                "Fangda Han",
                "Guoyao Hao",
                "Ricardo Guerrero",
                "Vladimir Pavlovic"
            ]
        },
        {
            "id": "1801.01615",
            "score": 0.75,
            "title": "Total Capture: A 3D Deformation Model for Tracking Faces, Hands, and Bodies",
            "authors": "Hanbyul Joo, Tomas Simon, Yaser Sheikh",
            "abstract": "We present a unified deformation model for the markerless capture of multiple scales of human movement, including facial expressions, body motion, and hand gestures. An initial model is generated by locally stitching together models of the individual parts of the human body, which we refer to as the \"Frankenstein\" model. This model enables the full expression of part movements, including face and hands by a single seamless model. Using a large-scale capture of people wearing everyday clothes, we optimize the Frankenstein model to create \"Adam\". Adam is a calibrated model that shares the same skeleton hierarchy as the initial model but can express hair and clothing geometry, making it directly usable for fitting people as they normally appear in everyday life. Finally, we demonstrate the use of these models for total motion tracking, simultaneously capturing the large-scale body movements and the subtle face and hand motion of a social group of people.",
            "year": 2018,
            "month": "Jan",
            "authors_parsed": [
                "Hanbyul Joo",
                "Tomas Simon",
                "Yaser Sheikh"
            ]
        }
    ],
    "authors": [
        {
            "author": "Fangda Han",
            "papers": [
                {
                    "id": "2012.02821",
                    "score": 0.77,
                    "title": "MPG: A Multi-ingredient Pizza Image Generator with Conditional StyleGANs",
                    "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "Multilabel conditional image generation is a challenging problem in computer vision. In this work we propose Multi-ingredient Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing multilabel images. We design MPG based on a state-of-the-art GAN structure called StyleGAN2, in which we develop a new conditioning technique by enforcing intermediate feature maps to learn scalewise label information. Because of the complex nature of the multilabel image generation problem, we also regularize synthetic image by predicting the corresponding ingredients as well as encourage the discriminator to distinguish between matched image and mismatched image. To verify the efficacy of MPG, we test it on Pizza10, which is a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realist pizza images with desired ingredients. The framework can be easily extend to other multilabel image generation scenarios.",
                    "year": 2020,
                    "month": "Dec",
                    "authors_parsed": [
                        "Fangda Han",
                        "Guoyao Hao",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "2110.11830",
                    "score": 0.75,
                    "title": "Multi-attribute Pizza Generator: Cross-domain Attribute Control with Conditional StyleGAN",
                    "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "Multi-attribute conditional image generation is a challenging problem in computervision. We propose Multi-attribute Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing images from a trichotomy of attributes: content, view-geometry, and implicit visual style. We design MPG by extending the state-of-the-art StyleGAN2, using a new conditioning technique that guides the intermediate feature maps to learn multi-scale multi-attribute entangled representationsof controlling attributes. Because of the complex nature of the multi-attribute image generation problem, we regularize the image generation by predicting the explicit conditioning attributes (ingredients and view). To synthesize a pizza image with view attributesoutside the range of natural training images, we design a CGI pizza dataset PizzaView using 3D pizza models and employ it to train a view attribute regressor to regularize the generation process, bridging the real and CGI training datasets. To verify the efficacy of MPG, we test it on Pizza10, a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realistic pizza images with desired ingredients and view attributes, beyond the range of those observed in real-world training data.",
                    "year": 2021,
                    "month": "Oct",
                    "authors_parsed": [
                        "Fangda Han",
                        "Guoyao Hao",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "1905.13149",
                    "score": 0.74,
                    "title": "The Art of Food: Meal Image Synthesis from Ingredients",
                    "authors": "Fangda Han, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "In this work we propose a new computational framework, based on generative deep models, for synthesis of photo-realistic food meal images from textual descriptions of its ingredients. Previous works on synthesis of images from text typically rely on pre-trained text models to extract text features, followed by a generative neural networks (GANs) aimed to generate realistic images conditioned on the text features. These works mainly focus on generating spatially compact and well-defined categories of objects, such as birds or flowers. In contrast, meal images are significantly more complex, consisting of multiple ingredients whose appearance and spatial qualities are further modified by cooking methods. We propose a method that first builds an attention-based ingredients-image association model, which is then used to condition a generative neural network tasked with synthesizing meal images. Furthermore, a cycle-consistent constraint is added to further improve image quality and control appearance. Extensive experiments show our model is able to generate meal image corresponding to the ingredients, which could be used to augment existing dataset for solving other computational food analysis problems.",
                    "year": 2019,
                    "month": "May",
                    "authors_parsed": [
                        "Fangda Han",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "2002.11493",
                    "score": 0.73,
                    "title": "CookGAN: Meal Image Synthesis from Ingredients",
                    "authors": "Fangda Han, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "In this work we propose a new computational framework, based on generative deep models, for synthesis of photo-realistic food meal images from textual list of its ingredients. Previous works on synthesis of images from text typically rely on pre-trained text models to extract text features, followed by generative neural networks (GAN) aimed to generate realistic images conditioned on the text features. These works mainly focus on generating spatially compact and well-defined categories of objects, such as birds or flowers, but meal images are significantly more complex, consisting of multiple ingredients whose appearance and spatial qualities are further modified by cooking methods. To generate real-like meal images from ingredients, we propose Cook Generative Adversarial Networks (CookGAN), CookGAN first builds an attention-based ingredients-image association model, which is then used to condition a generative neural network tasked with synthesizing meal images. Furthermore, a cycle-consistent constraint is added to further improve image quality and control appearance. Experiments show our model is able to generate meal images corresponding to the ingredients.",
                    "year": 2020,
                    "month": "Feb",
                    "authors_parsed": [
                        "Fangda Han",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                }
            ],
            "avg_score": 0.75
        },
        {
            "author": "Ricardo Guerrero",
            "papers": [
                {
                    "id": "2012.02821",
                    "score": 0.77,
                    "title": "MPG: A Multi-ingredient Pizza Image Generator with Conditional StyleGANs",
                    "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "Multilabel conditional image generation is a challenging problem in computer vision. In this work we propose Multi-ingredient Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing multilabel images. We design MPG based on a state-of-the-art GAN structure called StyleGAN2, in which we develop a new conditioning technique by enforcing intermediate feature maps to learn scalewise label information. Because of the complex nature of the multilabel image generation problem, we also regularize synthetic image by predicting the corresponding ingredients as well as encourage the discriminator to distinguish between matched image and mismatched image. To verify the efficacy of MPG, we test it on Pizza10, which is a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realist pizza images with desired ingredients. The framework can be easily extend to other multilabel image generation scenarios.",
                    "year": 2020,
                    "month": "Dec",
                    "authors_parsed": [
                        "Fangda Han",
                        "Guoyao Hao",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "2110.11830",
                    "score": 0.75,
                    "title": "Multi-attribute Pizza Generator: Cross-domain Attribute Control with Conditional StyleGAN",
                    "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "Multi-attribute conditional image generation is a challenging problem in computervision. We propose Multi-attribute Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing images from a trichotomy of attributes: content, view-geometry, and implicit visual style. We design MPG by extending the state-of-the-art StyleGAN2, using a new conditioning technique that guides the intermediate feature maps to learn multi-scale multi-attribute entangled representationsof controlling attributes. Because of the complex nature of the multi-attribute image generation problem, we regularize the image generation by predicting the explicit conditioning attributes (ingredients and view). To synthesize a pizza image with view attributesoutside the range of natural training images, we design a CGI pizza dataset PizzaView using 3D pizza models and employ it to train a view attribute regressor to regularize the generation process, bridging the real and CGI training datasets. To verify the efficacy of MPG, we test it on Pizza10, a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realistic pizza images with desired ingredients and view attributes, beyond the range of those observed in real-world training data.",
                    "year": 2021,
                    "month": "Oct",
                    "authors_parsed": [
                        "Fangda Han",
                        "Guoyao Hao",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "1905.13149",
                    "score": 0.74,
                    "title": "The Art of Food: Meal Image Synthesis from Ingredients",
                    "authors": "Fangda Han, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "In this work we propose a new computational framework, based on generative deep models, for synthesis of photo-realistic food meal images from textual descriptions of its ingredients. Previous works on synthesis of images from text typically rely on pre-trained text models to extract text features, followed by a generative neural networks (GANs) aimed to generate realistic images conditioned on the text features. These works mainly focus on generating spatially compact and well-defined categories of objects, such as birds or flowers. In contrast, meal images are significantly more complex, consisting of multiple ingredients whose appearance and spatial qualities are further modified by cooking methods. We propose a method that first builds an attention-based ingredients-image association model, which is then used to condition a generative neural network tasked with synthesizing meal images. Furthermore, a cycle-consistent constraint is added to further improve image quality and control appearance. Extensive experiments show our model is able to generate meal image corresponding to the ingredients, which could be used to augment existing dataset for solving other computational food analysis problems.",
                    "year": 2019,
                    "month": "May",
                    "authors_parsed": [
                        "Fangda Han",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "2002.11493",
                    "score": 0.73,
                    "title": "CookGAN: Meal Image Synthesis from Ingredients",
                    "authors": "Fangda Han, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "In this work we propose a new computational framework, based on generative deep models, for synthesis of photo-realistic food meal images from textual list of its ingredients. Previous works on synthesis of images from text typically rely on pre-trained text models to extract text features, followed by generative neural networks (GAN) aimed to generate realistic images conditioned on the text features. These works mainly focus on generating spatially compact and well-defined categories of objects, such as birds or flowers, but meal images are significantly more complex, consisting of multiple ingredients whose appearance and spatial qualities are further modified by cooking methods. To generate real-like meal images from ingredients, we propose Cook Generative Adversarial Networks (CookGAN), CookGAN first builds an attention-based ingredients-image association model, which is then used to condition a generative neural network tasked with synthesizing meal images. Furthermore, a cycle-consistent constraint is added to further improve image quality and control appearance. Experiments show our model is able to generate meal images corresponding to the ingredients.",
                    "year": 2020,
                    "month": "Feb",
                    "authors_parsed": [
                        "Fangda Han",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                }
            ],
            "avg_score": 0.75
        },
        {
            "author": "Vladimir Pavlovic",
            "papers": [
                {
                    "id": "2012.02821",
                    "score": 0.77,
                    "title": "MPG: A Multi-ingredient Pizza Image Generator with Conditional StyleGANs",
                    "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "Multilabel conditional image generation is a challenging problem in computer vision. In this work we propose Multi-ingredient Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing multilabel images. We design MPG based on a state-of-the-art GAN structure called StyleGAN2, in which we develop a new conditioning technique by enforcing intermediate feature maps to learn scalewise label information. Because of the complex nature of the multilabel image generation problem, we also regularize synthetic image by predicting the corresponding ingredients as well as encourage the discriminator to distinguish between matched image and mismatched image. To verify the efficacy of MPG, we test it on Pizza10, which is a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realist pizza images with desired ingredients. The framework can be easily extend to other multilabel image generation scenarios.",
                    "year": 2020,
                    "month": "Dec",
                    "authors_parsed": [
                        "Fangda Han",
                        "Guoyao Hao",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "2110.11830",
                    "score": 0.75,
                    "title": "Multi-attribute Pizza Generator: Cross-domain Attribute Control with Conditional StyleGAN",
                    "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "Multi-attribute conditional image generation is a challenging problem in computervision. We propose Multi-attribute Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing images from a trichotomy of attributes: content, view-geometry, and implicit visual style. We design MPG by extending the state-of-the-art StyleGAN2, using a new conditioning technique that guides the intermediate feature maps to learn multi-scale multi-attribute entangled representationsof controlling attributes. Because of the complex nature of the multi-attribute image generation problem, we regularize the image generation by predicting the explicit conditioning attributes (ingredients and view). To synthesize a pizza image with view attributesoutside the range of natural training images, we design a CGI pizza dataset PizzaView using 3D pizza models and employ it to train a view attribute regressor to regularize the generation process, bridging the real and CGI training datasets. To verify the efficacy of MPG, we test it on Pizza10, a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realistic pizza images with desired ingredients and view attributes, beyond the range of those observed in real-world training data.",
                    "year": 2021,
                    "month": "Oct",
                    "authors_parsed": [
                        "Fangda Han",
                        "Guoyao Hao",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "1905.13149",
                    "score": 0.74,
                    "title": "The Art of Food: Meal Image Synthesis from Ingredients",
                    "authors": "Fangda Han, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "In this work we propose a new computational framework, based on generative deep models, for synthesis of photo-realistic food meal images from textual descriptions of its ingredients. Previous works on synthesis of images from text typically rely on pre-trained text models to extract text features, followed by a generative neural networks (GANs) aimed to generate realistic images conditioned on the text features. These works mainly focus on generating spatially compact and well-defined categories of objects, such as birds or flowers. In contrast, meal images are significantly more complex, consisting of multiple ingredients whose appearance and spatial qualities are further modified by cooking methods. We propose a method that first builds an attention-based ingredients-image association model, which is then used to condition a generative neural network tasked with synthesizing meal images. Furthermore, a cycle-consistent constraint is added to further improve image quality and control appearance. Extensive experiments show our model is able to generate meal image corresponding to the ingredients, which could be used to augment existing dataset for solving other computational food analysis problems.",
                    "year": 2019,
                    "month": "May",
                    "authors_parsed": [
                        "Fangda Han",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "2002.11493",
                    "score": 0.73,
                    "title": "CookGAN: Meal Image Synthesis from Ingredients",
                    "authors": "Fangda Han, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "In this work we propose a new computational framework, based on generative deep models, for synthesis of photo-realistic food meal images from textual list of its ingredients. Previous works on synthesis of images from text typically rely on pre-trained text models to extract text features, followed by generative neural networks (GAN) aimed to generate realistic images conditioned on the text features. These works mainly focus on generating spatially compact and well-defined categories of objects, such as birds or flowers, but meal images are significantly more complex, consisting of multiple ingredients whose appearance and spatial qualities are further modified by cooking methods. To generate real-like meal images from ingredients, we propose Cook Generative Adversarial Networks (CookGAN), CookGAN first builds an attention-based ingredients-image association model, which is then used to condition a generative neural network tasked with synthesizing meal images. Furthermore, a cycle-consistent constraint is added to further improve image quality and control appearance. Experiments show our model is able to generate meal images corresponding to the ingredients.",
                    "year": 2020,
                    "month": "Feb",
                    "authors_parsed": [
                        "Fangda Han",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                }
            ],
            "avg_score": 0.75
        },
        {
            "author": "Guoyao Hao",
            "papers": [
                {
                    "id": "2012.02821",
                    "score": 0.77,
                    "title": "MPG: A Multi-ingredient Pizza Image Generator with Conditional StyleGANs",
                    "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "Multilabel conditional image generation is a challenging problem in computer vision. In this work we propose Multi-ingredient Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing multilabel images. We design MPG based on a state-of-the-art GAN structure called StyleGAN2, in which we develop a new conditioning technique by enforcing intermediate feature maps to learn scalewise label information. Because of the complex nature of the multilabel image generation problem, we also regularize synthetic image by predicting the corresponding ingredients as well as encourage the discriminator to distinguish between matched image and mismatched image. To verify the efficacy of MPG, we test it on Pizza10, which is a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realist pizza images with desired ingredients. The framework can be easily extend to other multilabel image generation scenarios.",
                    "year": 2020,
                    "month": "Dec",
                    "authors_parsed": [
                        "Fangda Han",
                        "Guoyao Hao",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                },
                {
                    "id": "2110.11830",
                    "score": 0.75,
                    "title": "Multi-attribute Pizza Generator: Cross-domain Attribute Control with Conditional StyleGAN",
                    "authors": "Fangda Han, Guoyao Hao, Ricardo Guerrero, Vladimir Pavlovic",
                    "abstract": "Multi-attribute conditional image generation is a challenging problem in computervision. We propose Multi-attribute Pizza Generator (MPG), a conditional Generative Neural Network (GAN) framework for synthesizing images from a trichotomy of attributes: content, view-geometry, and implicit visual style. We design MPG by extending the state-of-the-art StyleGAN2, using a new conditioning technique that guides the intermediate feature maps to learn multi-scale multi-attribute entangled representationsof controlling attributes. Because of the complex nature of the multi-attribute image generation problem, we regularize the image generation by predicting the explicit conditioning attributes (ingredients and view). To synthesize a pizza image with view attributesoutside the range of natural training images, we design a CGI pizza dataset PizzaView using 3D pizza models and employ it to train a view attribute regressor to regularize the generation process, bridging the real and CGI training datasets. To verify the efficacy of MPG, we test it on Pizza10, a carefully annotated multi-ingredient pizza image dataset. MPG can successfully generate photo-realistic pizza images with desired ingredients and view attributes, beyond the range of those observed in real-world training data.",
                    "year": 2021,
                    "month": "Oct",
                    "authors_parsed": [
                        "Fangda Han",
                        "Guoyao Hao",
                        "Ricardo Guerrero",
                        "Vladimir Pavlovic"
                    ]
                }
            ],
            "avg_score": 0.76
        },
        {
            "author": "Avinash Ummadisingu",
            "papers": [
                {
                    "id": "2203.05187",
                    "score": 0.75,
                    "title": "Cluttered Food Grasping with Adaptive Fingers and Synthetic-Data Trained Object Detection",
                    "authors": "Avinash Ummadisingu, Kuniyuki Takahashi, Naoki Fukaya",
                    "abstract": "The food packaging industry handles an immense variety of food products with wide-ranging shapes and sizes, even within one kind of food. Menus are also diverse and change frequently, making automation of pick-and-place difficult. A popular approach to bin-picking is to first identify each piece of food in the tray by using an instance segmentation method. However, human annotations to train these methods are unreliable and error-prone since foods are packed close together with unclear boundaries and visual similarity making separation of pieces difficult. To address this problem, we propose a method that trains purely on synthetic data and successfully transfers to the real world using sim2real methods by creating datasets of filled food trays using high-quality 3d models of real pieces of food for the training instance segmentation models. Another concern is that foods are easily damaged during grasping. We address this by introducing two additional methods -- a novel adaptive finger mechanism to passively retract when a collision occurs, and a method to filter grasps that are likely to cause damage to neighbouring pieces of food during a grasp. We demonstrate the effectiveness of the proposed method on several kinds of real foods.",
                    "year": 2022,
                    "month": "Mar",
                    "authors_parsed": [
                        "Avinash Ummadisingu",
                        "Kuniyuki Takahashi",
                        "Naoki Fukaya"
                    ]
                },
                {
                    "id": "2206.06556",
                    "score": 0.73,
                    "title": "F3 Hand: A Versatile Robot Hand Inspired by Human Thumb and Index Fingers",
                    "authors": "Naoki Fukaya, Avinash Ummadisingu, Guilherme Maeda, Shin-ichi Maeda",
                    "abstract": "It is challenging to grasp numerous objects with varying sizes and shapes with a single robot hand. To address this, we propose a new robot hand called the 'F3 hand' inspired by the complex movements of human index finger and thumb. The F3 hand attempts to realize complex human-like grasping movements by combining a parallel motion finger and a rotational motion finger with an adaptive function. In order to confirm the performance of our hand, we attached it to a mobile manipulator - the Toyota Human Support Robot (HSR) and conducted grasping experiments. In our results, we show that it is able to grasp all YCB objects (82 in total), including washers with outer diameters as small as 6.4mm. We also built a system for intuitive operation with a 3D mouse and grasp an additional 24 objects, including small toothpicks and paper clips and large pitchers and cracker boxes. The F3 hand is able to achieve a 98% success rate in grasping even under imprecise control and positional offsets. Furthermore, owing to the finger's adaptive function, we demonstrate characteristics of the F3 hand that facilitate the grasping of soft objects such as strawberries in a desirable posture.",
                    "year": 2022,
                    "month": "Jun",
                    "authors_parsed": [
                        "Naoki Fukaya",
                        "Avinash Ummadisingu",
                        "Guilherme Maeda",
                        "Shin-ichi Maeda"
                    ]
                }
            ],
            "avg_score": 0.74
        },
        {
            "author": "Naoki Fukaya",
            "papers": [
                {
                    "id": "2203.05187",
                    "score": 0.75,
                    "title": "Cluttered Food Grasping with Adaptive Fingers and Synthetic-Data Trained Object Detection",
                    "authors": "Avinash Ummadisingu, Kuniyuki Takahashi, Naoki Fukaya",
                    "abstract": "The food packaging industry handles an immense variety of food products with wide-ranging shapes and sizes, even within one kind of food. Menus are also diverse and change frequently, making automation of pick-and-place difficult. A popular approach to bin-picking is to first identify each piece of food in the tray by using an instance segmentation method. However, human annotations to train these methods are unreliable and error-prone since foods are packed close together with unclear boundaries and visual similarity making separation of pieces difficult. To address this problem, we propose a method that trains purely on synthetic data and successfully transfers to the real world using sim2real methods by creating datasets of filled food trays using high-quality 3d models of real pieces of food for the training instance segmentation models. Another concern is that foods are easily damaged during grasping. We address this by introducing two additional methods -- a novel adaptive finger mechanism to passively retract when a collision occurs, and a method to filter grasps that are likely to cause damage to neighbouring pieces of food during a grasp. We demonstrate the effectiveness of the proposed method on several kinds of real foods.",
                    "year": 2022,
                    "month": "Mar",
                    "authors_parsed": [
                        "Avinash Ummadisingu",
                        "Kuniyuki Takahashi",
                        "Naoki Fukaya"
                    ]
                },
                {
                    "id": "2206.06556",
                    "score": 0.73,
                    "title": "F3 Hand: A Versatile Robot Hand Inspired by Human Thumb and Index Fingers",
                    "authors": "Naoki Fukaya, Avinash Ummadisingu, Guilherme Maeda, Shin-ichi Maeda",
                    "abstract": "It is challenging to grasp numerous objects with varying sizes and shapes with a single robot hand. To address this, we propose a new robot hand called the 'F3 hand' inspired by the complex movements of human index finger and thumb. The F3 hand attempts to realize complex human-like grasping movements by combining a parallel motion finger and a rotational motion finger with an adaptive function. In order to confirm the performance of our hand, we attached it to a mobile manipulator - the Toyota Human Support Robot (HSR) and conducted grasping experiments. In our results, we show that it is able to grasp all YCB objects (82 in total), including washers with outer diameters as small as 6.4mm. We also built a system for intuitive operation with a 3D mouse and grasp an additional 24 objects, including small toothpicks and paper clips and large pitchers and cracker boxes. The F3 hand is able to achieve a 98% success rate in grasping even under imprecise control and positional offsets. Furthermore, owing to the finger's adaptive function, we demonstrate characteristics of the F3 hand that facilitate the grasping of soft objects such as strawberries in a desirable posture.",
                    "year": 2022,
                    "month": "Jun",
                    "authors_parsed": [
                        "Naoki Fukaya",
                        "Avinash Ummadisingu",
                        "Guilherme Maeda",
                        "Shin-ichi Maeda"
                    ]
                }
            ],
            "avg_score": 0.74
        },
        {
            "author": "Shan Jia",
            "papers": [
                {
                    "id": "1910.05457",
                    "score": 0.74,
                    "title": "Spoofing and Anti-Spoofing with Wax Figure Faces",
                    "authors": "Shan Jia, Xin Li, Chuanbo Hu, Zhengquan Xu",
                    "abstract": "We have witnessed rapid advances in both face presentation attack models and presentation attack detection (PAD) in recent years. Compared to widely studied 2D face presentation attacks (e.g. printed photos and video replays), 3D face presentation attacks are more challenging because face recognition systems (FRS) is more easily confused by the 3D characteristics of materials similar to real faces. Existing 3D face spoofing databases, mostly based on 3D facial masks, are restricted to small data size and suffer from poor authenticity due to the difficulty and expense of mask production. In this work, we introduce a wax figure face database (WFFD) as a novel and super-realistic 3D face presentation attack. This database contains 2300 image pairs (totally 4600) and 745 subjects including both real and wax figure faces with high diversity from online collections. On one hand, our experiments have demonstrated the spoofing potential of WFFD on three popular FRSs. On the other hand, we have developed a multi-feature voting scheme for wax figure face detection (anti-spoofing), which combines three discriminative features at the decision level. The proposed detection method was compared against several face PAD approaches and found to outperform other competing methods. Surprisingly, our fusion-based detection method achieves an Average Classification Error Rate (ACER) of 11.73\\% on the WFFD database, which is even better than human-based detection.",
                    "year": 2019,
                    "month": "Oct",
                    "authors_parsed": [
                        "Shan Jia",
                        "Xin Li",
                        "Chuanbo Hu",
                        "Zhengquan Xu"
                    ]
                },
                {
                    "id": "1906.11900",
                    "score": 0.74,
                    "title": "A database for face presentation attack using wax figure faces",
                    "authors": "Shan Jia, Chuanbo Hu, Guodong Guo, Zhengquan Xu",
                    "abstract": "Compared to 2D face presentation attacks (e.g. printed photos and video replays), 3D type attacks are more challenging to face recognition systems (FRS) by presenting 3D characteristics or materials similar to real faces. Existing 3D face spoofing databases, however, mostly based on 3D masks, are restricted to small data size or poor authenticity due to the production difficulty and high cost. In this work, we introduce the first wax figure face database, WFFD, as one type of super-realistic 3D presentation attacks to spoof the FRS. This database consists of 2200 images with both real and wax figure faces (totally 4400 faces) with a high diversity from online collections. Experiments on this database first investigate the vulnerability of three popular FRS to this kind of new attack. Further, we evaluate the performance of several face presentation attack detection methods to show the attack abilities of this super-realistic face spoofing database.",
                    "year": 2019,
                    "month": "Jun",
                    "authors_parsed": [
                        "Shan Jia",
                        "Chuanbo Hu",
                        "Guodong Guo",
                        "Zhengquan Xu"
                    ]
                }
            ],
            "avg_score": 0.74
        },
        {
            "author": "Chuanbo Hu",
            "papers": [
                {
                    "id": "1910.05457",
                    "score": 0.74,
                    "title": "Spoofing and Anti-Spoofing with Wax Figure Faces",
                    "authors": "Shan Jia, Xin Li, Chuanbo Hu, Zhengquan Xu",
                    "abstract": "We have witnessed rapid advances in both face presentation attack models and presentation attack detection (PAD) in recent years. Compared to widely studied 2D face presentation attacks (e.g. printed photos and video replays), 3D face presentation attacks are more challenging because face recognition systems (FRS) is more easily confused by the 3D characteristics of materials similar to real faces. Existing 3D face spoofing databases, mostly based on 3D facial masks, are restricted to small data size and suffer from poor authenticity due to the difficulty and expense of mask production. In this work, we introduce a wax figure face database (WFFD) as a novel and super-realistic 3D face presentation attack. This database contains 2300 image pairs (totally 4600) and 745 subjects including both real and wax figure faces with high diversity from online collections. On one hand, our experiments have demonstrated the spoofing potential of WFFD on three popular FRSs. On the other hand, we have developed a multi-feature voting scheme for wax figure face detection (anti-spoofing), which combines three discriminative features at the decision level. The proposed detection method was compared against several face PAD approaches and found to outperform other competing methods. Surprisingly, our fusion-based detection method achieves an Average Classification Error Rate (ACER) of 11.73\\% on the WFFD database, which is even better than human-based detection.",
                    "year": 2019,
                    "month": "Oct",
                    "authors_parsed": [
                        "Shan Jia",
                        "Xin Li",
                        "Chuanbo Hu",
                        "Zhengquan Xu"
                    ]
                },
                {
                    "id": "1906.11900",
                    "score": 0.74,
                    "title": "A database for face presentation attack using wax figure faces",
                    "authors": "Shan Jia, Chuanbo Hu, Guodong Guo, Zhengquan Xu",
                    "abstract": "Compared to 2D face presentation attacks (e.g. printed photos and video replays), 3D type attacks are more challenging to face recognition systems (FRS) by presenting 3D characteristics or materials similar to real faces. Existing 3D face spoofing databases, however, mostly based on 3D masks, are restricted to small data size or poor authenticity due to the production difficulty and high cost. In this work, we introduce the first wax figure face database, WFFD, as one type of super-realistic 3D presentation attacks to spoof the FRS. This database consists of 2200 images with both real and wax figure faces (totally 4400 faces) with a high diversity from online collections. Experiments on this database first investigate the vulnerability of three popular FRS to this kind of new attack. Further, we evaluate the performance of several face presentation attack detection methods to show the attack abilities of this super-realistic face spoofing database.",
                    "year": 2019,
                    "month": "Jun",
                    "authors_parsed": [
                        "Shan Jia",
                        "Chuanbo Hu",
                        "Guodong Guo",
                        "Zhengquan Xu"
                    ]
                }
            ],
            "avg_score": 0.74
        },
        {
            "author": "Zhengquan Xu",
            "papers": [
                {
                    "id": "1910.05457",
                    "score": 0.74,
                    "title": "Spoofing and Anti-Spoofing with Wax Figure Faces",
                    "authors": "Shan Jia, Xin Li, Chuanbo Hu, Zhengquan Xu",
                    "abstract": "We have witnessed rapid advances in both face presentation attack models and presentation attack detection (PAD) in recent years. Compared to widely studied 2D face presentation attacks (e.g. printed photos and video replays), 3D face presentation attacks are more challenging because face recognition systems (FRS) is more easily confused by the 3D characteristics of materials similar to real faces. Existing 3D face spoofing databases, mostly based on 3D facial masks, are restricted to small data size and suffer from poor authenticity due to the difficulty and expense of mask production. In this work, we introduce a wax figure face database (WFFD) as a novel and super-realistic 3D face presentation attack. This database contains 2300 image pairs (totally 4600) and 745 subjects including both real and wax figure faces with high diversity from online collections. On one hand, our experiments have demonstrated the spoofing potential of WFFD on three popular FRSs. On the other hand, we have developed a multi-feature voting scheme for wax figure face detection (anti-spoofing), which combines three discriminative features at the decision level. The proposed detection method was compared against several face PAD approaches and found to outperform other competing methods. Surprisingly, our fusion-based detection method achieves an Average Classification Error Rate (ACER) of 11.73\\% on the WFFD database, which is even better than human-based detection.",
                    "year": 2019,
                    "month": "Oct",
                    "authors_parsed": [
                        "Shan Jia",
                        "Xin Li",
                        "Chuanbo Hu",
                        "Zhengquan Xu"
                    ]
                },
                {
                    "id": "1906.11900",
                    "score": 0.74,
                    "title": "A database for face presentation attack using wax figure faces",
                    "authors": "Shan Jia, Chuanbo Hu, Guodong Guo, Zhengquan Xu",
                    "abstract": "Compared to 2D face presentation attacks (e.g. printed photos and video replays), 3D type attacks are more challenging to face recognition systems (FRS) by presenting 3D characteristics or materials similar to real faces. Existing 3D face spoofing databases, however, mostly based on 3D masks, are restricted to small data size or poor authenticity due to the production difficulty and high cost. In this work, we introduce the first wax figure face database, WFFD, as one type of super-realistic 3D presentation attacks to spoof the FRS. This database consists of 2200 images with both real and wax figure faces (totally 4400 faces) with a high diversity from online collections. Experiments on this database first investigate the vulnerability of three popular FRS to this kind of new attack. Further, we evaluate the performance of several face presentation attack detection methods to show the attack abilities of this super-realistic face spoofing database.",
                    "year": 2019,
                    "month": "Jun",
                    "authors_parsed": [
                        "Shan Jia",
                        "Chuanbo Hu",
                        "Guodong Guo",
                        "Zhengquan Xu"
                    ]
                }
            ],
            "avg_score": 0.74
        },
        {
            "author": "Priya Sundaresan",
            "papers": [
                {
                    "id": "2309.05197",
                    "score": 0.74,
                    "title": "Learning Sequential Acquisition Policies for Robot-Assisted Feeding",
                    "authors": "Priya Sundaresan, Jiajun Wu, Dorsa Sadigh",
                    "abstract": "A robot providing mealtime assistance must perform specialized maneuvers with various utensils in order to pick up and feed a range of food items. Beyond these dexterous low-level skills, an assistive robot must also plan these strategies in sequence over a long horizon to clear a plate and complete a meal. Previous methods in robot-assisted feeding introduce highly specialized primitives for food handling without a means to compose them together. Meanwhile, existing approaches to long-horizon manipulation lack the flexibility to embed highly specialized primitives into their frameworks. We propose Visual Action Planning OveR Sequences (VAPORS), a framework for long-horizon food acquisition. VAPORS learns a policy for high-level action selection by leveraging learned latent plate dynamics in simulation. To carry out sequential plans in the real world, VAPORS delegates action execution to visually parameterized primitives. We validate our approach on complex real-world acquisition trials involving noodle acquisition and bimanual scooping of jelly beans. Across 38 plates, VAPORS acquires much more efficiently than baselines, generalizes across realistic plate variations such as toppings and sauces, and qualitatively appeals to user feeding preferences in a survey conducted across 49 individuals. Code, datasets, videos, and supplementary materials can be found on our website: https://sites.google.com/view/vaporsbot.",
                    "year": 2023,
                    "month": "Sep",
                    "authors_parsed": [
                        "Priya Sundaresan",
                        "Jiajun Wu",
                        "Dorsa Sadigh"
                    ]
                },
                {
                    "id": "2211.14648",
                    "score": 0.74,
                    "title": "Learning Visuo-Haptic Skewering Strategies for Robot-Assisted Feeding",
                    "authors": "Priya Sundaresan, Suneel Belkhale, Dorsa Sadigh",
                    "abstract": "Acquiring food items with a fork poses an immense challenge to a robot-assisted feeding system, due to the wide range of material properties and visual appearances present across food groups. Deformable foods necessitate different skewering strategies than firm ones, but inferring such characteristics for several previously unseen items on a plate remains nontrivial. Our key insight is to leverage visual and haptic observations during interaction with an item to rapidly and reactively plan skewering motions. We learn a generalizable, multimodal representation for a food item from raw sensory inputs which informs the optimal skewering strategy. Given this representation, we propose a zero-shot framework to sense visuo-haptic properties of a previously unseen item and reactively skewer it, all within a single interaction. Real-robot experiments with foods of varying levels of visual and textural diversity demonstrate that our multimodal policy outperforms baselines which do not exploit both visual and haptic cues or do not reactively plan. Across 6 plates of different food items, our proposed framework achieves 71% success over 69 skewering attempts total. Supplementary material, datasets, code, and videos are available on our website: https://sites.google.com/view/hapticvisualnet-corl22/home",
                    "year": 2022,
                    "month": "Nov",
                    "authors_parsed": [
                        "Priya Sundaresan",
                        "Suneel Belkhale",
                        "Dorsa Sadigh"
                    ]
                }
            ],
            "avg_score": 0.74
        }
    ]
}
    

def get_authors(papers):
    authors = defaultdict(list)
    for paper in papers:
        for author in paper.authors_parsed:
            authors[author].append(paper)
    authors = [{"author": author,
                "papers": [paper.__dict__ for paper in papers],
                "avg_score": avg_score(papers)}
                for author, papers in authors.items()]
    authors = sorted(authors, key=lambda e: e["avg_score"], reverse=True)
    authors = sorted(authors, key=lambda e: len(e["papers"]), reverse=True)
    return authors[:10]

def error(msg):
    return json.dumps({"error": msg})