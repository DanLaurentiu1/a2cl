import { Profile } from "../../domain/Profile";

export const ALL_PROFILES: readonly Profile[] = [
  new Profile("Profile 1"),
  new Profile("Profile 2"),
  new Profile("Profile 3"),
] as const;

export function getProfileByName(name: string): Profile {
  const result = ALL_PROFILES.find((profile) => profile.name === name);
  if (result === undefined) {
    throw Error();
  }
  return result;
}
