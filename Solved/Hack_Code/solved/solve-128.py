#!/usr/bin/env python3
import functools
import random

# Convert CSV into list of routes
with open('routes.txt') as f:
    file_lines = f.readlines()
    routes = list(map(lambda line: tuple(line.strip().split(',')), file_lines))

# Get set of all IDs
network_ids = set()
for route in routes:
    network_ids.update(route)
network_ids = list(network_ids)
print('IDs:', len(network_ids))

# Count the occurance of target_id in routes
@functools.lru_cache(maxsize=None)  # for memoization
def count_occurance_with_id(routes, target_id):
    occurance = 0
    for route in routes:
        if target_id in route:
            occurance += 1
    return occurance

# Find the id in network_ids with the most occurance
def get_most_occurance_with_id(routes):
    found_id = ''
    found_occurs = -1
    for this_id in network_ids:
        occurs = count_occurance_with_id(routes, this_id)
        if occurs > found_occurs:
            found_id = this_id
            found_occurs = occurs
    
    # print those alternatives
    '''
    for this_id in network_ids:
        occurs = count_occurance_with_id(routes, this_id)
        if occurs == found_occurs and this_id != found_id:
            print(f'{found_id} == {this_id}')
    '''
    return (found_id, found_occurs)

def get_most_occurance_with_id_list(routes):
    found_occurs = -1
    for this_id in network_ids:
        occurs = count_occurance_with_id(routes, this_id)
        if occurs > found_occurs:
            found_occurs = occurs
    
    # get all ids
    found_ids = []
    for this_id in network_ids:
        occurs = count_occurance_with_id(routes, this_id)
        if occurs == found_occurs:
            found_ids.append(this_id)

    return (found_ids, found_occurs)

# Get routes that do not include target_id
def exclude_this_id(routes, target_id):
    return [r for r in routes if target_id not in r]

# Print solution
def print_solution(solution):
    print('Solution:', '\n'.join(solution))

########################################################
# [Solution for 128]
# Choose most occurance of ID in routes
# Then get ramaining routes and repeat.
if True:
    random.shuffle(network_ids)
    solution = []
    while len(routes) > 0:
        hashable_routes = tuple(tuple(x) for x in routes)  # for memoization
        found = get_most_occurance_with_id(hashable_routes)
        found_id = found[0]
        print(f"Found tap ({len(solution)}):", found)
        print("Remaining routes:", len(routes))
        routes = exclude_this_id(routes, found_id)
        solution.append(found_id)

    print_solution(solution)


# not working
if False:
    def find_next(routes, solution=[]):
        hashable_routes = tuple(tuple(x) for x in routes)  # for memoization
        found = get_most_occurance_with_id_list(hashable_routes)
        found_ids = found[0]

        if len(routes) == 0:
            if len(solution) <= 126:
                # Since we only need 126 or less, quit
                # prematurely as we need not calculate the rest
                # of the iterations
                print_solution(solution)
                quit()
            return solution
        else:
            print(f"Found tap ({len(solution)}):", found)
            print("Remaining routes:", len(routes))
            next_solutions = []

            # Since we only need 126 or less, quit prematurely
            # prematurely as we need not calculate the rest
            # of the iterations
            if len(solution) >= 126:
                return solution + [found_ids[0]]

            for found_id in found_ids:
                r = exclude_this_id(routes, found_id)
                s = find_next(r, solution + [found_id])
                next_solutions.append(s)

            return min(next_solutions, key=len) # return shortest solution

    solution = find_next(routes)
    print('Solution:', '\n'.join(solution))

