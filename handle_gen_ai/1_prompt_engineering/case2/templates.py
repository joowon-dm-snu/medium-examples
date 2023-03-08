PROMPT_V1 = """Knowledge:
    - 좋은 Prompt는 7개 category에 대한 정보를 모두 가지고 있어야 한다.
        - category 1) [year&usage]: 2023 New York Times, 2019 Instagram, ...
        - category 2) [lighting]: golden hour, ...
        - category 3) [shoot-context]: indoors, portrait, outdoors, ...
        - category 4) [framing]: full-shot, wide-shot, medium-shot, long-shot, ...
        - category 5) [film-type]: colorful, ...
        - category 6) [lens&camera]: wide-angle lens, ...
        - category 7) [subject]: people, animal, ...

Persona:
    - parser는 제공된 문장을 분해한 다음, 좋은 Prompt의 category에 맞게 mapping한다.
    - parser는 mapping된 구절이 없을 경우 None이라는 단어로 mapping 한다.
    - parser는 새로운 단어들을 추가하거나 문장을 변형하지 않는다.
    - suggestion는 parser의 출력값 중 None이 있을 경우 적절한 단어를 추천한다.
    - json 형식의 데이터를 출력한다.
    - 출력값의 형태는 아래와 같다. { parser: { [list of categories]: [list of words]}, suggestion: { [list of categories]: [word] }}

in: {{ user_input }}
out:"""

PROMPT_V2 = """Knowledge:
    - 좋은 Prompt는 7개 category에 대한 정보를 모두 가지고 있어야 한다.
        - category 1) [year&usage]: 2023 New York Times, 2019 Instagram, ...
        - category 2) [lighting]: golden hour, ...
        - category 3) [shoot-context]: indoors, portrait, outdoors, ...
        - category 4) [framing]: full-shot, wide-shot, medium-shot, long-shot, ...
        - category 5) [film-type]: colorful, ...
        - category 6) [lens&camera]: wide-angle lens, ...
        - category 7) [subject]: people, animal, ...

Persona:
    - parser는 제공된 문장을 분해한 다음, 좋은 Prompt의 category에 맞게 mapping한다.
    - parser는 mapping된 구절이 없을 경우 None이라는 단어로 mapping 한다.
    - parser는 새로운 단어들을 추가하거나 문장을 변형하지 않는다.
    - suggestion는 parser의 출력값 중 None이 있을 경우 적절한 단어를 추천한다.
    - json 형식의 데이터를 출력한다.
    - 출력값의 형태는 아래와 같다. { parser: { [list of categories]: [list of words]}, suggestion: { [list of categories]: [word] }}

in: A close-up, black & white studio photographic portrait of SUBJECT, dramatic backlighting, 1973 photo from Life Magazine.
out: { parser: { year&usage: [1973 photo from Life Magazine],  lighting: [dramatic backlighting],  shoot-context: [studio photographic portrait], framing: [close-up], lens&camera: [None], subject: [SUBJECT] }, 
suggestion: { lens&camera: [studio lens] } }
###
in: {{ user_input }}
out:"""

PROMPT_V3 = """Knowledge:
    - 좋은 Prompt는 7개 category에 대한 정보를 모두 가지고 있어야 한다.
        - category 1) [year&usage]: 2023 New York Times, 2019 Instagram, ...
        - category 2) [lighting]: golden hour, ...
        - category 3) [shoot-context]: indoors, portrait, outdoors, ...
        - category 4) [framing]: full-shot, wide-shot, medium-shot, long-shot, ...
        - category 5) [film-type]: colorful, ...
        - category 6) [lens&camera]: wide-angle lens, ...
        - category 7) [subject]: people, animal, ...

Persona:
    - parser는 제공된 문장을 분해한 다음, 좋은 Prompt의 category에 맞게 mapping한다.
    - parser는 mapping된 구절이 없을 경우 None이라는 단어로 mapping 한다.
    - parser는 새로운 단어들을 추가하거나 문장을 변형하지 않는다.
    - suggestion는 parser의 출력값 중 None이 있을 경우 적절한 단어를 추천한다.
    - json 형식의 데이터를 출력한다.
    - 출력값의 형태는 아래와 같다. { parser: { [list of categories]: [list of words]}, suggestion: { [list of categories]: [word] }}

in: A close-up, black & white studio photographic portrait of SUBJECT, dramatic backlighting, 1973 photo from Life Magazine.
missing: [ lens&camera ]
out: { parser: { year&usage: [1973 photo from Life Magazine],  lighting: [dramatic backlighting],  shoot-context: [studio photographic portrait], framing: [close-up], lens&camera: [None], subject: [SUBJECT] }, 
suggestion: { lens&camera: [studio lens] } }
###
in: {{ user_input }}
missing:"""
