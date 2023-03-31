# THIS PROMPT IS NOT WORKING BUT IDEA IS GOOD
# gpt_index/indices/query/query_transform/prompts.py
DEFAULT_IMAGE_OUTPUT_TMPL = (
    "{query_str}"
    "Show any image with a HTML <img/> tag with {image_width}."
    'e.g., <image src="data/img.jpg" width="{image_width}" />.'
)
