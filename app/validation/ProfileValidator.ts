import { Profile } from "../domain/Profile";

export class ProfileValidator {
  static validateProfile(profile: Partial<Profile>): void {
    if (!/^(?! )[A-Za-z0-9]+$/.test(profile.name!)) {
      throw new Error("Invalid characters in the title");
    }
    if (profile.name!.length > 30) {
      throw new Error("Profile name must be ≤ 30 characters");
    }
  }
}
