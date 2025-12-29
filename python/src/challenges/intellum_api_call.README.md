# Coding Challenge: API Integration & Data Processing

## Objective
Demonstrate your ability to interact with external APIs, handle JSON responses, and write clean, maintainable code. You must be proficient in writing code to interact with APIs. This challenge will be used during the technical interview stage.

---

## Scenario
You are given access to a public REST API that returns JSON data. Your task is to fetch data from the API, process it according to the requirements below, and return a structured result.

---

## API Details
Endpoint:
https://jsonplaceholder.typicode.com/posts

Description:
The API returns a list of blog posts. Each post contains the following fields:
- userId (number)
- id (number)
- title (string)
- body (string)

---

## Requirements

### 1. Fetch Data
- Make an HTTP GET request to the API endpoint.
- Handle HTTP errors such as non-200 status codes.
- Handle network failures gracefully.

### 2. Process Data
- Group posts by userId.
- For each userId:
  - Count the total number of posts.
  - Determine the longest post title based on character length.

### 3. Output
Produce a list of objects with the following structure:
- userId: number
- postCount: number
- longestTitle: string

The final output must be sorted by userId in ascending order.

### 4. Code Quality
- Use clear function or class separation.
- Follow best practices for readability and maintainability.
- Include basic inline comments where appropriate.
- Avoid unnecessary complexity.

---

## Constraints
- You may use any programming language.
- You may use standard libraries or common HTTP clients.
- Do not use third-party SDKs specific to this API.
- The solution should run as a simple script or from the command line.

---

## Bonus (Optional)
- Implement retry logic for failed API requests.
- Write a simple unit test for your data processing logic.
- Allow the API URL to be provided via configuration or a command-line argument.

---

## What We’re Evaluating
- Ability to work with REST APIs
- Error handling and edge-case awareness
- Data transformation and aggregation skills
- Code clarity, structure, and maintainability
- Overall problem-solving approach

---

## Time Expectation
30–45 minutes

## Sample json output

From the API call:

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
  }
]
```


