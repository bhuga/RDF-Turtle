module RDF::Turtle
  ##
  # Turtle format specification.
  # FIXME docs
  class Format < RDF::Format
    content_type 'text/turtle', :extension => :ttl
    content_encoding 'UTF-8'
 
    reader { RDF::Turtle::Reader }
    writer { RDF::Turtle::Writer }
  end
end

