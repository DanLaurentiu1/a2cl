import { Profile } from "../../domain/Profile";

export const ALL_PROFILES: readonly Profile[] = [
  new Profile("Profile 1", false),
  new Profile("Profile 2", true),
  new Profile("Profile 3", true),
] as const;

export function getProfileByName(name: string): Profile {
  const result = ALL_PROFILES.find((profile) => profile.name === name);
  if (result === undefined) {
    throw Error();
  }
  return result;
}
