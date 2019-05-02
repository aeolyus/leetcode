package main

func merge(nums1 []int, m int, nums2 []int, n int) {
	i, a, b := m+n-1, m-1, n-1
	for ; i >= 0 && a >= 0 && b >= 0; i-- {
		if nums1[a] > nums2[b] {
			nums1[i] = nums1[a]
			a--
		} else {
			nums1[i] = nums2[b]
			b--
		}
	}
	for ; a >= 0; a-- {
		nums1[i] = nums1[a]
		i--
	}
	for ; b >= 0; b-- {
		nums1[i] = nums2[b]
		i--
	}
}
