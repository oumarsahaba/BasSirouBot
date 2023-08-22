<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">BasSirouBot</h3>

  <p align="center">
    A conversational bot agent about Ecole Polytechnique de Thiès.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#step-by-step-guide">Step-by-step guide</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The idea is to set up a personalized conversational agent to respond to all questions regarding the École Polytechnique de Thiès using GPT Index.
The goal of this project is to gather and prepare data, implement embedding techniques, and write prompts to customize ChatGPT.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* Python
* Flask
* llama_index
* Docker

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is a step-by-step guide on how you start the project

### Prerequisites

Before starting the project you need to ensure that you have docker installed on your server.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Step-by-step guide

The project has been dockerized meaning that all requirements and steps for launching are described and defined. You just need to build it and run it.

1. Clone the repo and pull the develop branch
   ```sh
   git clone (https link)
   git checkout -b develop
   git pull origin develop
   ```
2. Enter a valide open ai key:
   Go to the index_server file and replace the API key with a valid one
3. Build your project
   ```sh
   docker build --tag image-name .
      ```
5. Run the image on a container
   ```sh
   docker run [--detach] image-name .
   ```
6. Get the API on the 5601 port

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contributing


If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>




