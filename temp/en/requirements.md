# Requirements

## **Functional**

### Series Information

- [x] Get detailed information about a specific anime or manga series.
- [ ] Search for series by title, genre, airing year, etc.
- [ ] Filter series by popularity, rating, duration, etc.

### User Interaction

- [x] Allow users to mark series as favorites or add them to a watchlist.
- [ ] Allow users to leave reviews and ratings for specific series.

### Recommendations and Discovery

- [ ] Get personalized recommendations based on the user's viewing history.
- [ ] Suggest new anime and manga series based on user preferences.

### Lists and Additional Details

- [x] Get the episode list of a specific anime series.
- [x] Get information about the original manga related to an anime series.

### Additional Information

- [x] Get information about the staff involved in creating an anime or manga series.
- [ ] Get information about the availability of a series on different streaming platforms.

## **Non-Functional**

### Usability and Documentation

- [x] The API should be easy to use for developers, with clear and comprehensive documentation that includes usage examples, descriptions of endpoints, request parameters, and expected responses.
- [x] Documentation should be up-to-date and easily accessible so that developers can quickly integrate it into their applications.

### Scalability

- [x] The API architecture should be highly scalable, capable of handling a high volume of concurrent requests without performance degradation.
- [ ] Horizontal and vertical scalability practices should be implemented to ensure that the API can grow to meet future user demands.

### Security and Authentication

- [ ] A robust authentication system should be implemented to protect sensitive API operations and prevent unauthorized access.
- [ ] Security standards like OAuth 2.0 should be employed to manage third-party access to user data and ensure that only authorized users can access certain functionalities.

### Performance

- [ ] The API should have optimal performance, providing fast and consistent response times even under heavy loads.
- [ ] Database queries and processing logic should be optimized to minimize wait times and maximize API efficiency.

### Availability

- [ ] The API should be highly available, with uptime close to 100% to ensure that users can access it at all times.
- [x] Redundancy and fault tolerance strategies should be implemented to mitigate the impacts of possible service interruptions.

### Maintainability

- [x] The API code should follow clean development practices and be well-organized to facilitate its maintenance over time.
- [x] Clear procedures should be established for version management, updates, and security patches to ensure the stability and continuous security of the API.

## Limitations

- [x] Request limits per minute/hour
- [x] Access limits to detailed data of certain series or specific features.
- [x] Authentication requirements for certain operations, such as using access tokens or API keys to query or modify data on behalf of users.
- [x] Performance and scalability considerations, implementing caching, query optimization, or load distribution to handle traffic spikes.
- [x] Compatibility limitations with specific versions.
- [ ] Access restrictions from certain geographical locations.
- [ ] Data restrictions, such as limited availability of certain types of information or the need to obtain special permissions to access sensitive or restricted data.
