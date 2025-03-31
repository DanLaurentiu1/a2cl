import { Profile } from "../../domain/Profile";

export class ProfileValidator {
  public validateProfile(profile: Profile): void {
    this.validateProfileName(profile);
    this.validateProfileProficiencies(profile);
  }

  private validateProfileProficiencies(profile: Profile): void {
    for (const [_, value] of profile.proficiencies) {
      if (typeof value !== "number" || value < 0 || value > 100) {
        throw new Error("Invalid proficiency value");
      }
    }
  }

  public validateProfileName(profile: Profile): void {
    if (!/^(?! )[A-Za-z0-9]+$/.test(profile.name!)) {
      throw new Error("Invalid characters in the title");
    }
    if (profile.name!.length > 30) {
      throw new Error("Profile name must be ≤ 30 characters");
    }
  }
}
export let profileValidator = new ProfileValidator();
