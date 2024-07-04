[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<br />
<div align="center">
  <h3 align="center">Media Expert Price Comparison</h3>
  <strong align="center">
    Media Expert Price Comparison allows you to monitor the prices of the products you observe on a daily basis.
    <br />
    <br />
    <a href="https://github.com/DEENUU1/media-expert-price-comparison/issues">Report Bug</a>
    ·
    <a href="https://github.com/DEENUU1/media-expert-price-comparison/issues">Request Feature</a>
  </strong>
</div>


## About the project
The project consists of 2 applications:
- web application allowing you to add new sources to observations and view results
- a scraper that runs every day thanks to the use of Celery and Redis

## Technologies:
- Python
  - FastAPI
  - Selenium
  - Sqlalchemy
  - Celery
  - Celery beat
- Redis
- PostgreSQL
- SQLite
- Docker
- HTMX, HTML, CSS


## Installation
### With docker
```bash
git clone https://github.com/DEENUU1/media-expert-price-comparison.git
```


```bash
cp .env.example .env
```

In `.env` set `DEBUG="True" by default it's `DEBUG="False"
 
```bash
docker-compose up -d --build
```

### Without docker
```bash
git clone https://github.com/DEENUU1/media-expert-price-comparison.git
```

```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
cp .env.example .env
```

```bash
cd app
```

```bash
uvicorn app:app --reload
```

## Authors

- [@DEENUU1](https://www.github.com/DEENUU1)

<!-- LICENSE -->

## License

See `LICENSE.txt` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/DEENUU1/media-expert-price-comparison.svg?style=for-the-badge

[contributors-url]: https://github.com/DEENUU1/media-expert-price-comparison/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/DEENUU1/media-expert-price-comparison.svg?style=for-the-badge

[forks-url]: https://github.com/DEENUU1/media-expert-price-comparison/network/members

[stars-shield]: https://img.shields.io/github/stars/DEENUU1/media-expert-price-comparison.svg?style=for-the-badge

[stars-url]: https://github.com/DEENUU1/media-expert-price-comparison/stargazers

[issues-shield]: https://img.shields.io/github/issues/DEENUU1/media-expert-price-comparison.svg?style=for-the-badge

[issues-url]: https://github.com/DEENUU1/media-expert-price-comparison/issues

[license-shield]: https://img.shields.io/github/license/DEENUU1/media-expert-price-comparison.svg?style=for-the-badge

[license-url]: https://github.com/DEENUU1/media-expert-price-comparison/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/kacper-wlodarczyk

[basic]: https://github.com/DEENUU1/media-expert-price-comparison/blob/main/assets/v1_2/basic.gif?raw=true

[full]: https://github.com/DEENUU1/media-expert-price-comparison/blob/main/assets/v1_2/full.gif?raw=true

[search]: https://github.com/DEENUU1/media-expert-price-comparison/blob/main/assets/v1_2/search.gif?raw=true
