output "q01_sorted_list" {
    value = module.q01_sorting
}

output "q01_sorted_list_of_keys_of_map" {
    value = module.q01_sorting.sorted_list_of_keys
}

output "q01_sorted_list_of_values_of_map" {
    value = module.q01_sorting.sorted_list_of_values
}

output "q01_sorted_map" {
    value = module.q01_sorting.sorted_map
}

output "q02_reusable_security_group" {
    value = module.q02_reusable_security_group.result
}

