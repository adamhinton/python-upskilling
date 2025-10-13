// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/description/


// Given the array restaurants where  restaurants[i] = [idi, ratingi, 
// veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.

// The veganFriendly filter will be either true 
// (meaning you should only include restaurants with veganFriendlyi set to true) 
// or false (meaning you can include any restaurant). 
// In addition, you have the filters maxPrice and maxDistance 
// which are the maximum value for price and distance of restaurants you should consider respectively.

// Return the array of restaurant IDs after filtering, 
// ordered by rating from highest to lowest. 
// For restaurants with the same rating, order them by id from highest to lowest. 
// For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.

type Restaurant = [id: number, rating: number, veganFriendly: 0 | 1, price: number, distance: number]

// Plan:
// Write isValidRestaurant helper function for filtering


const isValidRestaurant = (restaurant: Restaurant, shouldBeVeganFriendly: boolean, maxPrice: number, maxDistance: number): boolean => {
        const [id, rating, veganFriendly, price, distance] = restaurant;

        const isValidVeganFriendly = shouldBeVeganFriendly === false || (veganFriendly === 1)
        const isValidPrice = price <= maxPrice
        const isValidDistance = distance <= maxDistance

        return isValidVeganFriendly && isValidPrice && isValidDistance
    }