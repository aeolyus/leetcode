package main;

func containsDuplicate(nums []int) bool {
    set := make(map[int]bool);
    for _, i := range nums {
        if !set[i] {
            set[i] = true;
        }
    }
    return len(nums) != len(set);
}
