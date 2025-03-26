import { Profile } from "../domain/Profile";
import { Topic } from "../domain/Topic";
import { ProfileValidator } from "../validation/ProfileValidator";
import { topicRepository, TopicRepository } from "./TopicRepository";

export class ProfileRepository {
  private _profiles: Map<String, Profile>;
  private _topicRepository: TopicRepository;

  constructor() {
    this._profiles = new Map();
    this._topicRepository = topicRepository;
    this.initialiseProfiles();
  }

  public getProfileByName(name: String): Profile | undefined {
    return this._profiles.get(name);
  }

  public addProfile(profile: Profile) {
    ProfileValidator.validateProfile(profile);
    this._profiles.set(profile.name, profile);
  }

  private initialiseProfiles() {
    const proficiencies1 = new Map<Topic, number>([
      [this._topicRepository.getTopicByName("Array")!, 75.5],
      [this._topicRepository.getTopicByName("Hash Table")!, 35.5],
      [this._topicRepository.getTopicByName("Linked List")!, 12.6],
      [this._topicRepository.getTopicByName("Math")!, 95.4],
      [this._topicRepository.getTopicByName("Recursion")!, 25.5],
      [this._topicRepository.getTopicByName("String")!, 84.2],
      [this._topicRepository.getTopicByName("Sliding Window")!, 84.2],
      [this._topicRepository.getTopicByName("Divide And Conquer")!, 84.2],
      [this._topicRepository.getTopicByName("Binary Search")!, 84.2],
      [this._topicRepository.getTopicByName("Two Pointers")!, 84.2],
      [this._topicRepository.getTopicByName("Dynamic Programming")!, 84.2],
    ]);

    const proficiencies2 = new Map<Topic, number>([
      [this._topicRepository.getTopicByName("Array")!, 35.5],
      [this._topicRepository.getTopicByName("Hash Table")!, 31.5],
      [this._topicRepository.getTopicByName("Linked List")!, 53.6],
      [this._topicRepository.getTopicByName("Math")!, 12],
      [this._topicRepository.getTopicByName("Recursion")!, 65],
      [this._topicRepository.getTopicByName("String")!, 73.4],
      [this._topicRepository.getTopicByName("Sliding Window")!, 12.2],
      [this._topicRepository.getTopicByName("Divide And Conquer")!, 38.2],
      [this._topicRepository.getTopicByName("Binary Search")!, 8.2],
      [this._topicRepository.getTopicByName("Two Pointers")!, 53.4],
      [this._topicRepository.getTopicByName("Dynamic Programming")!, 31],
    ]);

    this._profiles.set(
      "Profile 1",
      new Profile("Profile 1", true, proficiencies1)
    );
    this._profiles.set(
      "Profile 2",
      new Profile("Profile 2", true, proficiencies2)
    );
  }
}
export let profileRepository = new ProfileRepository();
