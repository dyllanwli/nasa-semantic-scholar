from semanticscholar import SemanticScholar
sch = SemanticScholar()


results = sch.search_paper('NASA Earth Data')
print(f'{results.total} results.', f'First occurrence: {results[0].title}.')


for i in results:
    print(i)
    break