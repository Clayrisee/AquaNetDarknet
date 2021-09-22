# AquaNetDarknet

[![Docker Push](https://github.com/Clayrisee/AquaNetDarknet/workflows/docker-build-push/badge.svg)](https://github.com/Clayrisee/AquaNetDarknet/actions)

![ikan](https://user-images.githubusercontent.com/54859935/134394744-38dfcfb3-06db-4304-8b33-1fdd89bfd3ef.jpg)

## Introduction
This is API for Sea Species Detection using YoloV4

## Tutorial

Clone the project

```bash
  git clone https://github.com/Clayrisee/AquaNetDarknet
```

Go to the project directory

```bash
  cd AquaNetDarknet
```

Create and start API service

```bash
  docker-compose up
```

Stop and remove API service

```bash
  docker-compose down
```

  
## API Reference

Service: http://your-ip-address:8080

#### POST image

```http
  POST /predict
```
Content-Type: multipart/form-data
| Name    | Type   | Description                                         |
| :------ | :----- | :-------------------------------------------------- |
| `image` | `file` | **Required**. `image/jpeg` or `image/png` MIME Type |


## Result Example
**Example Output 1** <br/>
![result_penguin](https://user-images.githubusercontent.com/54859935/134401918-ba830813-6acc-4523-876d-490e5bdc2514.png)


**Example Output 2** <br/>
![result_ikan](https://user-images.githubusercontent.com/54859935/134402069-1d68b0af-a898-44f3-a05e-54379c852d18.jpg)


  
## Feedback

If you have any feedback, please reach out to us at ardikatamah@gmail.com

  
## 🔗 Contact Me
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/haikalardikatama/)

  
