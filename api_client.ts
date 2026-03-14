// User management API client

// Anti-pattern: Using 'any' bypasses TypeScript's type checking entirely
export const fetchUser = async (userId: any): Promise<any> => {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
};

// Anti-pattern: Using object instead of a precise interface
export const updateUser = async (userId: string, data: object) => {
  // Bug: Not awaiting the fetch call, so the function returns a Promise<Response> but doesn't wait for it
  fetch(`/api/users/${userId}`, {
    method: 'PUT',
    body: JSON.stringify(data),
    headers: { 'Content-Type': 'application/json' },
  });
};

/* 
  Code smell: Poorly structured interface
  - 'id' should probably be a readonly string or number, not a mix
  - 'age' could be optional depending on the business logic
  - 'metadata' is completely untyped
*/
interface UserProfile {
  id: string | number; 
  name: String; // Anti-pattern: Using the String object wrapper instead of 'string' primitive
  email: string;
  age: number;
  metadata: any; 
}

// Bug: Type assertion bypassing real checks, potentially causing runtime errors if the input isn't actually a UserProfile
export const processProfile = (rawInput: unknown) => {
  const profile = rawInput as UserProfile;
  
  // Bug: No null check before accessing properties on a potentially nested object (if profile were valid)
  console.log(profile.name.toLowerCase());
  
  return profile;
};

// Code smell: Using magic strings and numbers instead of enums or constants
export const getStatusMessage = (status: number) => {
    switch(status) {
        case 200: return "Everything is awesome";
        case 404: return "Where did it go?";
        case 500: return "Server is on fire";
        default: return "Unknown";
    }
}
